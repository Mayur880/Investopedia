var endDate= "23 September 2060 10:00 AM"
document.getElementById("end-Date").innerText=endDate;
const inputs=document.querySelectorAll("input");

function clock(){
    const end=new Date(endDate)
    const now=new Date()
   const diff=(end - now) / 1000;
   inputs[0].value=Math.floor(diff / 3600 /24);
   inputs[1].value=Math.floor(diff / 3600) % 24;
   inputs[2].value=Math.floor(diff / 60) % 60;
   inputs[3].value=Math.floor(diff ) % 60;
//    console.log(diff);



}
 
clock()

setInterval(
   () =>{
    clock()
   },1000
)