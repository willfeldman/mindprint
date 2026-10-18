"use strict";
let teamPrompt='';
async function getTeamPrompt(){if(teamPrompt)return teamPrompt;const response=await fetch('collaboration-prompt.md');if(!response.ok)throw Error('The prompt could not load. Use the download link and try again.');teamPrompt=await response.text();document.getElementById('collaboration-prompt').textContent=teamPrompt;return teamPrompt;}
getTeamPrompt().catch(error=>{document.getElementById('collaboration-status').textContent=error.message;});
document.getElementById('copy-collaboration').addEventListener('click',async()=>{const status=document.getElementById('collaboration-status');try{const prompt=await getTeamPrompt();await navigator.clipboard.writeText(prompt);status.textContent='Copied. Paste it into your AI conversation, then add the profiles your group has chosen to share.';}catch{status.textContent='Copy unavailable. Open “Read the prompt” to select the text, or download it.';}});
