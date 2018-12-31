var svgs = document.getElementsByTagName("svg");

for(i =0; i < svgs.length; i++){
    svgs[i].remove();
    console.log(svgs.length);
}

