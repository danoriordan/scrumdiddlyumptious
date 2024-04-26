"use strict";(self.webpackChunkAutoGen_Studio=self.webpackChunkAutoGen_Studio||[]).push([[245],{57009:function(e,t,l){l.r(t),l.d(t,{default:function(){return I}});var n=l(96540),a=l(3441),s=l(70870),r=l(43881),o=l(92744),i=l(63532),c=l(85575);var m=n.forwardRef((function({title:e,titleId:t,...l},a){return n.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",strokeWidth:1.5,stroke:"currentColor","aria-hidden":"true","data-slot":"icon",ref:a,"aria-labelledby":t},l),e?n.createElement("title",{id:t},e):null,n.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"m8.25 4.5 7.5 7.5-7.5 7.5"}))})),d=l(64467),u=l(45795);var v=n.forwardRef((function({title:e,titleId:t,...l},a){return n.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",strokeWidth:1.5,stroke:"currentColor","aria-hidden":"true","data-slot":"icon",ref:a,"aria-labelledby":t},l),e?n.createElement("title",{id:t},e):null,n.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"M12 21a9.004 9.004 0 0 0 8.716-6.747M12 21a9.004 9.004 0 0 1-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 0 1 7.843 4.582M12 3a8.997 8.997 0 0 0-7.843 4.582m15.686 0A11.953 11.953 0 0 1 12 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0 1 21 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0 1 12 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 0 1 3 12c0-1.605.42-3.113 1.157-4.418"}))}));var f=n.forwardRef((function({title:e,titleId:t,...l},a){return n.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",strokeWidth:1.5,stroke:"currentColor","aria-hidden":"true","data-slot":"icon",ref:a,"aria-labelledby":t},l),e?n.createElement("title",{id:t},e):null,n.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"m16.862 4.487 1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L6.832 19.82a4.5 4.5 0 0 1-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 0 1 1.13-1.897L16.863 4.487Zm0 0L19.5 7.125"}))}));var g=n.forwardRef((function({title:e,titleId:t,...l},a){return n.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",strokeWidth:1.5,stroke:"currentColor","aria-hidden":"true","data-slot":"icon",ref:a,"aria-labelledby":t},l),e?n.createElement("title",{id:t},e):null,n.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"m4.5 12.75 6 6 9-13.5"}))})),b=l(52332);var h=n.forwardRef((function({title:e,titleId:t,...l},a){return n.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",strokeWidth:1.5,stroke:"currentColor","aria-hidden":"true","data-slot":"icon",ref:a,"aria-labelledby":t},l),e?n.createElement("title",{id:t},e):null,n.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"M20.25 8.511c.884.284 1.5 1.128 1.5 2.097v4.286c0 1.136-.847 2.1-1.98 2.193-.34.027-.68.052-1.02.072v3.091l-3-3c-1.354 0-2.694-.055-4.02-.163a2.115 2.115 0 0 1-.825-.242m9.345-8.334a2.126 2.126 0 0 0-.476-.095 48.64 48.64 0 0 0-8.048 0c-1.131.094-1.976 1.057-1.976 2.192v4.286c0 .837.46 1.58 1.155 1.951m9.345-8.334V6.637c0-1.621-1.152-3.026-2.76-3.235A48.455 48.455 0 0 0 11.25 3c-2.115 0-4.198.137-6.24.402-1.608.209-2.76 1.614-2.76 3.235v6.226c0 1.621 1.152 3.026 2.76 3.235.577.075 1.157.14 1.74.194V21l4.155-4.155"}))})),w=l(14403),p=l(34267),E=l(11848),y=l(68777),k=l(62688),x=l(8369),N=l(24412),A=l(28007);var C=()=>{const[e,t]=n.useState({status:!0,message:"All good"}),[l,a]=n.useState(!1),r=((0,x.J)((e=>e.workflowConfig)),(0,x.J)((e=>e.setWorkflowConfig))),{user:c}=n.useContext(o.v),m=(0,s.Tt)()+"/workflows?user_id="+(null==c?void 0:c.email),[d,u]=n.useState([]),[v,f]=n.useState(0);return n.useEffect((()=>{c&&(t(null),a(!0),(0,s.hI)(m,{method:"GET",headers:{"Content-Type":"application/json"}},(e=>{e&&e.status?(u(e.data),e.data.length>0&&r(e.data[0])):i.Ay.error(e.message),a(!1)}),(e=>{t(e),i.Ay.error(e.message),a(!1)})))}),[]),n.createElement("div",{className:" mb-4 relative"},n.createElement("div",{className:"text-sm mt-2 mb-2 pb-1  "}," ","Please select an agent workflow to begin."," "),n.createElement("div",{className:"relative mt-2 "},n.createElement(k.p8,{loading:l}),d&&d.length>0&&n.createElement(N.A,{className:"w-full",value:d[v].name,onChange:e=>{f(e),r(d[e])},options:d.map(((e,t)=>({label:e.name,value:t})))}),n.createElement("div",{className:"mt-2 text-xs"}," ","View all workflows"," ",n.createElement("span",{className:"text-accent"}," ",n.createElement(A.Link,{to:"/build"},"here"))," ")),!d||d&&0===d.length&&n.createElement("div",{className:"p-1 border rounded text-xs px-2 text-secondary"}," ","No agent workflows found."))};function j(e,t){var l=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),l.push.apply(l,n)}return l}function S(e){for(var t=1;t<arguments.length;t++){var l=null!=arguments[t]?arguments[t]:{};t%2?j(Object(l),!0).forEach((function(t){(0,d.A)(e,t,l[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(l)):j(Object(l)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(l,t))}))}return e}var O=e=>{let{}=e;const[t,l]=n.useState(!1),[a,r]=n.useState({status:!0,message:"All good"}),{user:c}=n.useContext(o.v),m=(0,s.Tt)(),d=m+"/sessions?user_id="+(null==c?void 0:c.email),N=m+"/sessions",A=m+"/sessions/rename?name=",j=m+"/sessions/publish",O=m+"/sessions/delete",L=(0,x.J)((e=>e.sessions)),_=(0,x.J)((e=>e.workflowConfig)),I=(0,x.J)((e=>e.setSessions)),T=(0,x.J)((e=>e.session)),J=(0,x.J)((e=>e.setSession)),P=(0,x.J)((e=>e.setWorkflowConfig)),[R,W]=n.useState(!1);n.useEffect((()=>{if(L&&L.length>0){const e=L[0];J(e),P(null==e?void 0:e.flow_config)}else J(null)}),[L]);n.useEffect((()=>{c&&(r(null),l(!0),(0,s.hI)(d,{method:"GET",headers:{"Content-Type":"application/json"}},(e=>{e&&e.status?I(e.data):i.Ay.error(e.message),l(!1)}),(e=>{r(e),i.Ay.error(e.message),l(!1)})))}),[]);const[D,B]=n.useState({}),M=L.map(((e,t)=>{var a,o,m;const d=(null==T?void 0:T.id)===e.id,h=d?"bg-accent text-white":"bg-secondary text-primary";let w=[{label:n.createElement("div",{onClick:()=>{console.log("deleting session"),(e=>{r(null),l(!0);const t={method:"DELETE",headers:{"Content-Type":"application/json"},body:JSON.stringify({user_id:null==c?void 0:c.email,session:e})};(0,s.hI)(O,t,(e=>{e&&e.status?(i.Ay.success(e.message),I(e.data),e.data&&e.data.length>0&&J(e.data[0])):i.Ay.error(e.message),l(!1)}),(e=>{r(e),i.Ay.error(e.message),l(!1)}))})(e)}},n.createElement(u.A,{role:"button",title:"Delete",className:"h-4 w-4 mr-1 inline-block"}),"Delete"),key:"delete"},{label:n.createElement("div",{onClick:()=>{console.log("publishing session"),(()=>{r(null),l(!0);const e={user_id:null==c?void 0:c.email,session:T,tags:["published"]},t={method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(e)};(0,s.hI)(j,t,(e=>{e&&e.status?i.Ay.success(e.message):i.Ay.error(e.message),l(!1)}),(e=>{r(e),i.Ay.error(e.message),l(!1)}))})()}},n.createElement(v,{role:"button",title:"Publish",className:"h-4 w-4 mr-1 inline-block"}),"Publish"),key:"publish"},{label:n.createElement("div",{onClick:()=>{console.log("renaming session"),B(S(S({},B),{},{[e.id]:S(S({},D[e.id]),{},{visible:1})}))}},n.createElement(f,{role:"button",title:"Rename",className:"h-4 w-4 mr-1 inline-block"}),"Rename"),key:"rename"}];w.push();const E=n.createElement(p.A,{menu:{items:w},trigger:["click"],placement:"bottomRight"},n.createElement("div",{role:"button",className:"float-right ml-2 duration-100 hover:bg-secondary font-semibold px-2 pb-1  rounded "+(d?"hover:text-accent":"")},n.createElement("span",{className:"block -mt-2 "+(d?"text-white":"")}," ","...")));let y=e.id;return null!=e.name&&(y=e.name),n.createElement("div",{key:"sessionsrow"+t,className:"group relative  mb-2 pb-1  border-b border-dashed "},w.length>0&&n.createElement("div",{className:"  absolute right-2 top-2 group-hover:opacity-100 opacity-0 "},E),n.createElement("div",{className:"rounded p-2 cursor-pointer "+h,role:"button",onClick:()=>{J(e),P(e.flow_config)}},(!D[e.id]||0==(null===(a=D[e.id])||void 0===a?void 0:a.visible))&&n.createElement("div",{className:"text-xs"},(0,s.EJ)(y,20)),1==(null===(o=D[e.id])||void 0===o?void 0:o.visible)&&n.createElement("form",{onSubmit:t=>{var n;const a=(null===(n=D[e.id])||void 0===n?void 0:n.nameValue)||"";t.preventDefault(),console.log("submitRename",a),B(S(S({},B),{},{[e.id]:0})),((e,t)=>{r(null),l(!0);const n={user_id:null==c?void 0:c.email,session:e},a={method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(n)};console.log("renameSession to "+t,a),(0,s.hI)(A+t,a,(e=>{var t;e&&e.status?(i.Ay.success(e.message),I(e.data),P(null===(t=e.data[0])||void 0===t?void 0:t.workflow_config)):i.Ay.error(e.message),l(!1)}),(e=>{r(e),i.Ay.error(e.message),l(!1)}))})(e,a)}},n.createElement("div",{style:{display:"flex",flexDirection:"row",alignItems:"center"}},n.createElement("input",{id:"renameInputText-"+e.id,type:"text",value:null===(m=D[e.id])||void 0===m?void 0:m.nameValue,onChange:t=>{console.log("handleRename",t.target.value),B(S(S({},D),{},{[e.id]:S(S({},D[e.id]),{},{nameValue:t.target.value})}))},style:{color:"black"}}),n.createElement("button",{type:"submit"},n.createElement(g,{role:"button",className:"h-5 w-5 ml-1 inline-block"})))),n.createElement("div",{className:"text-xs mt-1"},n.createElement(b.A,{className:"h-4 w-4 inline-block mr-1"}),e.flow_config.name),n.createElement("div",{className:"text-xs text-right "},(0,s.fF)(e.timestamp))))}));let V,G;return"undefined"!=typeof window&&(V=window.innerHeight,G=V-400+"px"),n.createElement("div",{className:"  "},n.createElement(E.A,{title:n.createElement("div",{className:"font-semibold mb-2 pb-1 border-b"},n.createElement(b.A,{className:"h-5 w-5 inline-block mr-1"}),"New Sessions"," "),open:R,footer:[n.createElement(y.Ay,{key:"back",onClick:()=>{W(!1)}},"Cancel"),n.createElement(y.Ay,{key:"submit",type:"primary",disabled:!_,onClick:()=>{W(!1),(()=>{r(null),l(!0);const e={user_id:null==c?void 0:c.email,session:{user_id:null==c?void 0:c.email,flow_config:_,session_id:null}},t={method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(e)};console.log("createSession",t),(0,s.hI)(N,t,(e=>{var t;e&&e.status?(i.Ay.success(e.message),I(e.data),P(null===(t=e.data[0])||void 0===t?void 0:t.workflow_config)):i.Ay.error(e.message),l(!1)}),(e=>{r(e),i.Ay.error(e.message),l(!1)}))})()}},"Create")]},n.createElement(C,null)),n.createElement("div",{className:"mb-2 relative"},n.createElement("div",{className:""},n.createElement("div",{className:"font-semibold mb-2 pb-1 border-b"},n.createElement(h,{className:"h-5 w-5 inline-block mr-1"}),"Sessions"," "),L&&L.length>0&&n.createElement("div",{className:"text-xs  hidden mb-2 pb-1  "}," ","Create a new session or select an existing session to view chat."),n.createElement("div",{style:{maxHeight:G},className:"mb-4 overflow-y-auto scroll rounded relative "},M,n.createElement(k.p8,{loading:t})),(!L||0==L.length)&&!t&&n.createElement("div",{className:"text-xs text-gray-500"},"No sessions found. Create a new session to get started.")),n.createElement("div",{className:"flex gap-x-2"},n.createElement("div",{className:"flex-1"}),n.createElement(k.Yi,{className:"text-sm p-2 px-3",onClick:()=>{var e;L&&L.length>0?P(null===(e=L[0])||void 0===e?void 0:e.flow_config):P(null);W(!0)}}," ",n.createElement(w.A,{className:"w-5 h-5 inline-block mr-1"}),"New"))))};var L=()=>{const[e,t]=n.useState(!0),l=e?"270px":"50px";let a,s;"undefined"!=typeof window&&(a=window.innerHeight,s=a-180+"px");(0,x.J)((e=>e.workflowConfig));return n.createElement("div",{style:{minWidth:l,maxWidth:l,height:"calc(100vh - 190px)"},className:"    "},n.createElement("div",{className:" transition overflow-hidden duration-300  flex flex-col   h-full p-2 overflow-y-scroll scroll rounded "},n.createElement("div",{className:(e?"":"hidden")+"  "},n.createElement(O,null))),n.createElement("div",{onClick:()=>t(!e),role:"button",className:" hover:text-accent duration-150  "},e?n.createElement("div",{className:"mt-4  "}," ",n.createElement(c.A,{className:"w-6 h-6  inline-block    rounded"})," ",n.createElement("span",{className:"text-xs "}," close sidebar")):n.createElement(m,{className:"w-6 h-6   inline-block   font-bold rounded "})))};var _=()=>{const e=(0,x.J)((e=>e.session)),[t,l]=n.useState(!1),[a,c]=n.useState(null),[m,d]=n.useState("default"),[u,v]=n.useState(null),f=(0,x.J)((e=>e.connectionId));n.useEffect((()=>{(0,s.ZB)("ara_config",u)}),[u]);const[g,b]=n.useState({status:!0,message:"All good"}),{user:h}=n.useContext(o.v),w=(0,s.Tt)()+"/messages?user_id="+(null==h?void 0:h.email)+"&session_id="+(null==e?void 0:e.id),p=(0,x.J)((e=>e.workflowConfig));return n.useEffect((()=>{h&&e&&(b(null),l(!0),c(null),(0,s.hI)(w,{method:"GET",headers:{"Content-Type":"application/json"}},(e=>{e&&e.status?c(e.data):i.Ay.error(e.message),l(!1)}),(e=>{b(e),i.Ay.error(e.message),l(!1)})))}),[e]),n.createElement("div",{className:"h-full   "},n.createElement("div",{className:"flex h-full   "},n.createElement("div",{className:"  mr-2  rounded"},n.createElement(L,null)),n.createElement("div",{className:" flex-1  "},!e&&n.createElement("div",{className:" w-full  h-full flex items-center justify-center"},n.createElement("div",{className:"w-2/3",id:"middle"},n.createElement("div",{className:"w-full   text-center"}," ",n.createElement("img",{src:"/images/svgs/welcome.svg",alt:"welcome",className:"text-accent inline-block object-cover w-56"})),n.createElement(O,null))),null!==p&&null!==e&&n.createElement(r.A,{initMessages:a,connectionId:f}))))};var I=e=>{let{data:t}=e;return n.createElement(a.A,{meta:t.site.siteMetadata,title:"Home",link:"/"},n.createElement("main",{style:{height:"100%"},className:" h-full "},n.createElement(_,null)))}},52332:function(e,t,l){var n=l(96540);const a=n.forwardRef((function({title:e,titleId:t,...l},a){return n.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",strokeWidth:1.5,stroke:"currentColor","aria-hidden":"true","data-slot":"icon",ref:a,"aria-labelledby":t},l),e?n.createElement("title",{id:t},e):null,n.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"M6.429 9.75 2.25 12l4.179 2.25m0-4.5 5.571 3 5.571-3m-11.142 0L2.25 7.5 12 2.25l9.75 5.25-4.179 2.25m0 0L21.75 12l-4.179 2.25m0 0 4.179 2.25L12 21.75 2.25 16.5l4.179-2.25m11.142 0-5.571 3-5.571-3"}))}));t.A=a},45795:function(e,t,l){var n=l(96540);const a=n.forwardRef((function({title:e,titleId:t,...l},a){return n.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",strokeWidth:1.5,stroke:"currentColor","aria-hidden":"true","data-slot":"icon",ref:a,"aria-labelledby":t},l),e?n.createElement("title",{id:t},e):null,n.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0"}))}));t.A=a}}]);
//# sourceMappingURL=component---src-pages-index-tsx-f8334a336ca13507b802.js.map