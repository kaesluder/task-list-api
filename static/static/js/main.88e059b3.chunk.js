(this["webpackJsonptask-list-react"]=this["webpackJsonptask-list-react"]||[]).push([[0],{22:function(t,e,n){},23:function(t,e,n){},25:function(t,e,n){},26:function(t,e,n){},32:function(t,e,n){"use strict";n.r(e);var c=n(3),i=n.n(c),o=n(14),s=n.n(o),a=(n(22),n(17)),r=n(5),l=(n(23),n(2)),u=function(t){var e=t.isComplete?"tasks__item__toggle--completed":"";return Object(l.jsxs)("li",{className:"tasks__item",children:[Object(l.jsx)("button",{className:"tasks__item__toggle ".concat(e),onClick:function(){t.setter(t.id,t.isComplete)},children:t.title}),Object(l.jsx)("button",{className:"tasks__item__remove button",onClick:function(){t.onUnregister(t.id)},children:"x"})]})},d=(n(25),function(t){var e=t.tasks.map((function(e){return console.log(e),Object(l.jsx)(u,{id:e.id,title:e.title,isComplete:e.isComplete,setter:t.setter,onUnregister:t.onUnregister},e.id)}));return Object(l.jsx)("ul",{className:"tasks__list no-bullet",children:e})}),j=(n(26),n(34)),h=n(9),f=n(12),b={title:"",description:""},p=function(t){var e=Object(c.useState)(b),n=Object(r.a)(e,2),i=n[0],o=n[1],s=function(t){var e=t.target.value,n=t.target.name,c=Object(f.a)(Object(f.a)({},i),{},Object(h.a)({},n,e));o(c)};return Object(l.jsxs)("form",{onSubmit:function(e){e.preventDefault(),t.handleTaskSubmit(i),o(b)},children:[Object(l.jsxs)("div",{children:[Object(l.jsx)("label",{htmlFor:"title",children:"Task Title"}),Object(l.jsx)("input",{type:"type",id:"title",name:"title",value:i.title,onChange:s})]}),Object(l.jsxs)("div",{children:[Object(l.jsx)("label",{htmlFor:"description",children:"Task Description"}),Object(l.jsx)("input",{type:"type",id:"description",name:"description",value:i.description,onChange:s})]}),Object(l.jsx)("div",{children:Object(l.jsx)("input",{type:"submit",value:"Add Task"})})]})},m="http://localhost:5000",O=function(t){return{description:t.description,id:t.id,isComplete:t.is_complete,title:t.title}},g=function(){var t=Object(c.useState)([]),e=Object(r.a)(t,2),n=e[0],i=e[1];Object(c.useEffect)((function(){o()}),[]);var o=function(){return j.a.get("".concat(m,"/tasks")).then((function(t){return t.data.map(O)})).catch((function(t){console.log(t)})).then((function(t){i(t)})).catch((function(t){console.log(t)}))};return Object(l.jsxs)("div",{className:"App",children:[Object(l.jsx)("header",{className:"App-header",children:Object(l.jsx)("h1",{children:"Ada's Task List"})}),Object(l.jsx)("main",{children:Object(l.jsxs)("div",{children:[Object(l.jsx)(p,{handleTaskSubmit:function(t){var e;(e=t,j.a.post("".concat(m,"/tasks"),e).then((function(t){return O(t.data.task)})).catch((function(t){return console.log(t)}))).then((function(t){i([].concat(Object(a.a)(n),[t]))})).catch((function(t){return console.log(t)}))}}),Object(l.jsx)(d,{tasks:n,setter:function(t,e){return function(t,e){var n=e?"mark_complete":"mark_incomplete";return j.a.patch("".concat(m,"/tasks/").concat(t,"/").concat(n)).then((function(t){return O(t.data.task)})).catch((function(t){console.log(t)}))}(t,!e).then((function(t){i((function(e){return e.map((function(e){return t.id===e.id?t:e}))}))})).catch((function(t){console.log(t)}))},onUnregister:function(t){return function(t){return j.a.delete("".concat(m,"/tasks/").concat(t)).catch((function(t){console.log(t)}))}(t).then((function(){return o()})).catch((function(t){console.log(t)}))}})]})})]})},k=function(t){t&&t instanceof Function&&n.e(3).then(n.bind(null,35)).then((function(e){var n=e.getCLS,c=e.getFID,i=e.getFCP,o=e.getLCP,s=e.getTTFB;n(t),c(t),i(t),o(t),s(t)}))};n(31);s.a.render(Object(l.jsx)(i.a.StrictMode,{children:Object(l.jsx)(g,{})}),document.getElementById("root")),k()}},[[32,1,2]]]);
//# sourceMappingURL=main.88e059b3.chunk.js.map