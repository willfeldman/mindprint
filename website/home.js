"use strict";
// Preserve URLs from the original single-page guide, including shared snapshots.
function routeLegacy(){if(location.hash && (location.hash.startsWith('#mindprint=') || ['#create','#format','#mindos','#contents'].includes(location.hash)))location.replace('docs.html'+location.hash);}
routeLegacy();window.addEventListener('hashchange',routeLegacy);
const examples={without:{label:'A general approach, without a personal preference.',text:'List your ideas, compare their potential impact and effort, then choose the one with the strongest balance of value and feasibility.'},with:{label:'Using the preference: test the riskiest assumption first.',text:'I’d test the assumption most likely to change your decision. What is the smallest version we can put in front of someone this week?'}};
document.querySelectorAll('[data-example]').forEach(button=>button.addEventListener('click',()=>{document.querySelectorAll('[data-example]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));const value=examples[button.dataset.example];document.getElementById('response-label').textContent=value.label;document.getElementById('response-text').textContent=value.text;}));
