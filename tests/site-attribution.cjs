const test = require('node:test');
const assert = require('node:assert/strict');
const vm = require('node:vm');
const fs = require('node:fs');
const source = fs.readFileSync(__dirname + '/../site.js', 'utf8');
const currentTime = Date.parse('2026-11-02T10:00:00Z');
function setup({search='', consent=false, stored=null, deniedStorage=false, href='https://play.google.com/store/apps/details?id=com.lusor83.stellarmerge'}={}) {
  const memory = new Map(stored ? [['dlf_campaign', JSON.stringify(stored)]] : []);
  const events=[], remote=[], listeners={};
  const link={href, addEventListener:(name,fn)=>listeners[name]=fn};
  class FixedDate extends Date { static now(){return currentTime;} }
  const context={URL,URLSearchParams,Date:FixedDate,Number,Object,JSON,CustomEvent:class {constructor(type,init){this.type=type;this.detail=init.detail;}},location:{search,pathname:'/astral-fusion.html',origin:'https://lusor83.github.io',href:'https://lusor83.github.io/astral-fusion.html'+search},document:{querySelectorAll:()=>[link]},localStorage:{getItem:key=>{if(deniedStorage)throw Error('blocked');return memory.get(key)||null},setItem:(k,v)=>{if(deniedStorage)throw Error('blocked');memory.set(k,v)},removeItem:k=>{if(deniedStorage)throw Error('blocked');memory.delete(k)}},window:{lusorAnalyticsConsent:consent,dispatchEvent:e=>events.push(e),gtag:(...v)=>remote.push(v)}};
  vm.runInNewContext(source,context);
  return {memory,events,remote,link,window:context.window,click:()=>listeners.click?.()};
}
test('current campaign reaches Play referrer; no storage or remote collection without consent',()=>{const t=setup({search:'?utm_source=reddit&utm_campaign=november'});assert.equal(new URLSearchParams(new URL(t.link.href).searchParams.get('referrer')).get('utm_source'),'reddit');t.click();assert.equal(t.events[0].detail.event,'play_store_click');assert.equal(t.memory.size,0);assert.equal(t.remote.length,0)});
test('consented campaign expires after seven days',()=>{const t=setup({consent:true,stored:{utm_source:'old',captured_at:'2026-10-20T10:00:00Z'}});assert.equal(new URLSearchParams(new URL(t.link.href).searchParams.get('referrer')).get('utm_source'),'dlf_website');assert.equal(t.memory.size,0)});
test('valid stored campaign retained without extending its timestamp',()=>{const t=setup({consent:true,stored:{utm_source:'newsletter',captured_at:'2026-11-01T10:00:00Z'}});assert.equal(JSON.parse(t.memory.get('dlf_campaign')).captured_at,'2026-11-01T10:00:00.000Z');t.click();assert.equal(t.remote.length,1)});
test('malformed and future timestamps do not gain attribution',()=>{for(const captured_at of ['oops','2026-12-01T10:00:00Z']){const t=setup({consent:true,stored:{utm_source:'old',captured_at}});assert.equal(t.memory.size,0)}});
test('explicit referrer preserved and reported accurately',()=>{const href='https://play.google.com/store/apps/details?id=com.looktwist.game&hl=it&referrer=utm_source%3Deditorial';const t=setup({href,search:'?utm_source=reddit'});assert.equal(new URL(t.link.href).searchParams.get('hl'),'it');t.click();assert.equal(t.events[0].detail.utm_source,'editorial')});
test('blocked browser storage does not break official links',()=>{const t=setup({deniedStorage:true,search:'?utm_source=discord'});t.click();assert.equal(t.events.length,1)});
test('UTM email/full URL and oversized values are excluded',()=>{const t=setup({search:'?utm_source=user%40example.com&utm_campaign=https%3A%2F%2Fevil.example&utm_content='+ 'x'.repeat(90)});t.click();assert.equal(t.events[0].detail.utm_source,'dlf_website');assert.equal(t.events[0].detail.utm_campaign,'organic_site')});
test('consent grant permits collection; revocation clears storage and stops sends',()=>{const t=setup({search:'?utm_source=press'});t.window.lusorSetAnalyticsConsent(true);assert.equal(t.memory.size,1);t.click();assert.equal(t.remote.length,1);t.window.lusorSetAnalyticsConsent(false);t.click();assert.equal(t.remote.length,1);assert.equal(t.memory.size,0)});
test('press kit and product clicks have dedicated local events',()=>{for(const [href,event]of [['https://lusor83.github.io/press/astral-fusion.html','press_kit_click'],['https://lusor83.github.io/life-unwritten.html','game_page_click']]){const t=setup({href});t.click();assert.equal(t.events[0].detail.event,event)}});
test('host lookalikes are not rewritten',()=>{const href='https://evil.example/play.google.com/store/apps/details?id=com.fake';const t=setup({href});t.click();assert.equal(t.link.href,href);assert.equal(t.events.length,0)});

