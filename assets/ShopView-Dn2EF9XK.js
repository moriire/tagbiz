import{s as u,j as c,k as d,G as g,l as p,c as f,g as t,t as h,u as n,f as v,o as _,q as m}from"./index-CSa8JcRq.js";import{_ as w}from"./ProductPage-V4MxBpRq.js";import"./ProductSingle-BF1pH-B8.js";import"./plus-CLXrtRrJ.js";import"./_plugin-vue_export-helper-DlAUqK2U.js";const x=u("filter",()=>{const l=c(),s=d(l.products),e=g({pageCount:1,totalPages:l.length,start:0,next:function(){return this.pageSize*this.pageCount},pageSize:1,fstate:"",pstate:"disabled"});return{filtered:s,page:e,filterProductsByCategory:o=>{if(console.log(o.target.value),o.target.value==="all")s.value=l.products;else{let a=l.products.filter(r=>r.category.name===o.target.value);s.value=a}},filterProductsByAvailability:o=>{if(o.target.value<1&&(s.value=l.products.filter(a=>a.quantity==0),console.log(s.value)),o.target.value>0){let a=l.products.filter(r=>r.quantity>0);s.value=a}},doPagination:async()=>{let o=l.products.slice(e.start,e.next());console.log(e.next()),s.value=o,e.pageCount<e.totalPages/e.pageSize?(e.pageCount+=1,e.start+=e.pageSize):(e.pageCount-=1,e.start-=e.pageSize)}}}),y={class:"collection mt-100"},b={class:"container"},S={class:"row"},k={class:"col-lg-12 col-md-12 col-12"},P={class:"filter-sort-wrapper d-flex justify-content-between flex-wrap"},B={class:"collection-title-wrap d-flex align-items-end"},C={class:"collection-counter text_16 mb-0 ms-2"},N={__name:"ShopView",setup(l){const s=c();return x(),m(),d(!0),s.pages.limit=3,p(async()=>{await s.getProducts()}),(e,i)=>(_(),f("div",y,[t("div",b,[t("div",S,[t("div",k,[t("div",P,[t("div",B,[i[0]||(i[0]=t("h2",{class:"collection-title heading_24 mb-0"},"All products",-1)),t("p",C,"("+h(n(s).products.length)+" items)",1)]),i[1]||(i[1]=t("div",{class:"filter-sorting"},[t("div",{class:"collection-sorting position-relative d-none d-lg-block"},[t("div",{class:"sorting-header text_16 d-flex align-items-center justify-content-end"},[t("span",{class:"sorting-title me-2"},"Sort by:"),t("span",{class:"active-sorting"},"Featured"),t("span",{class:"sorting-icon"},[t("svg",{uclass:"icon icon-down",xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor","stroke-width":"2","stroke-linecap":"round","stroke-linejoin":"round",class:"feather feather-chevron-down"},[t("polyline",{points:"6 9 12 15 18 9"})])])]),t("ul",{class:"sorting-lists list-unstyled m-0"},[t("li",null,[t("a",{href:"#",class:"text_14"},"Featured")]),t("li",null,[t("a",{href:"#",class:"text_14"},"Best Selling")]),t("li",null,[t("a",{href:"#",class:"text_14"},"Alphabetically, A-Z")]),t("li",null,[t("a",{href:"#",class:"text_14"},"Alphabetically, Z-A")]),t("li",null,[t("a",{href:"#",class:"text_14"},"Price, low to high")]),t("li",null,[t("a",{href:"#",class:"text_14"},"Price, high to low")]),t("li",null,[t("a",{href:"#",class:"text_14"},"Date, old to new")]),t("li",null,[t("a",{href:"#",class:"text_14"},"Date, new to old")])])]),t("div",{class:"filter-drawer-trigger mobile-filter d-flex align-items-center d-lg-none"},[t("span",{class:"mobile-filter-icon me-2"},[t("svg",{xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor","stroke-width":"2","stroke-linecap":"round","stroke-linejoin":"round",class:"icon icon-filter"},[t("polygon",{points:"22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"})])]),t("span",{class:"mobile-filter-heading"},"Sorting")])],-1))]),v(w,{products:n(s).products,show:!0},null,8,["products"])])])])]))}};export{N as default};