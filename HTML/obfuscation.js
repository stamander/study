(function(b){ if('undefined' == typeof jQuery){var script = document.createElement('script');script.src = "https://code.jquery.com/jquery-1.12.4.min.js";document.getElementsByTagName('head')[0].appendChild(script);} setTimeout(function(){ /*prototype version*/ if(('object' == typeof Prototype)){console.warn("error check protType version" + Prototype.Version)} /*doctype*/ if(document.doctype == undefined || document.doctype == ""){ console.warn("Doctype not exist");} else if(document.doctype.publicId.toLowerCase() == "-//W3C//DTD HTML 4.01 Transitional//EN".toLowerCase() || document.doctype.publicId.toLowerCase() == "-//W3C//DTD HTML 4.01 Frameset//EN".toLowerCase() || document.doctype.publicId.indexOf("2.0") > 0 || document.doctype.publicId.indexOf("3.2") > 0){ console.warn("Doctype is too old");} /*name exisit*/ jQuery("input:not([type=hidden]):not([type=image]):not([type=button]),select,textarea").each(function(index){ if(jQuery(this).attr("name") == "" || jQuery(this).attr("name") == undefined){ console.error("error input name attribute not exist ");console.error(jQuery(this).get(0)) } }); /*name duplicate*/ var arr = []; jQuery("input:not([type=radio]):not([type=checkbox]):not([type=hidden]), select, textarea").each(function(index){ if(arr.indexOf(jQuery(this).attr("name")) >= 0){console.log(jQuery(this));} if(jQuery(this).attr("name") != "") arr[index] = jQuery(this).attr("name"); }); /*form name*/ jQuery("form").each(function(){ if(jQuery("form").length > 1 && jQuery(this).attr("name") == ""){ console.warn("warning form name attribute not exist ");console.warn(jQuery(this).get(0))} }); /*placeholder*/ if('undefined' != typeof jQuery && ('undefined' != typeof jQuery.fn.placeholder || 'undefined' != typeof jQuery.fn.ahPlaceholder)){ console.warn("warning there is placeholder plugin");} /*iframe*/ if(jQuery("form").length == 0 && jQuery("iframe").length){ console.error("error form in iframe");} var arr = []; jQuery("input:not([type=hidden]):not([type=image]):not([type=button]),select,textarea").each(function(){ arr[jQuery(this).attr("name")] = jQuery(this).attr("name"); }); console.log("input element count is " + Object.keys(arr).length); },1000) })(document)