var canvas
var ctx
var video;
var webcamWidth;
var webcamHeight;
var beforeCapture = true;

navigator.getUserMedia = (
  navigator.getUserMedia ||
  navigator.webkitGetUserMedia ||
  navigator.mozGetUserMedia ||
  navigator.msGetUserMedia
);

video = document.querySelector("#videoElement");
canvas = document.getElementById("myCanvas")
ctx = canvas.getContext('2d')

function camera(){
  if (navigator.mediaDevices.getUserMedia) {
    let constraints = { 
      audio: false, 
      video: {
        width: { min: 400, ideal: 400, max: 400 },
        height: { min: 400, ideal: 400, max: 400 },
    }
      
  };
      navigator.mediaDevices.getUserMedia(constraints)
        .then(function (stream) {
          video.srcObject = stream;
          webcamWidth = stream.getVideoTracks()[0].getSettings().width
          webcamHeight = stream.getVideoTracks()[0].getSettings().height
          canvas.setAttribute('width', 400);
          canvas.setAttribute('height', 400);
        })
        .catch(function (error) {
          console.log(error,"Something went wrong!");
        });
    }
}

function getCurrentFrame() {
  beforeCapture = false;
  ctx.drawImage(video, 0,0)
  img_dataURI = canvas.toDataURL('image/png')
  video.style.display = "none";
  var image= document.getElementById("my-data-uri")
  image.src = img_dataURI;
  image.classList.add("border")

  document.getElementById("cap").style.display='none';
  document.getElementById("done").style.display='inline';
  document.getElementById("recap").style.display='inline';
  document.getElementById("helpcap").style.display='none';
}

function recapture(){
  location.reload();
}

function postData(){
  
    var form = document.getElementById("myForm");
    var imageInput = document.getElementById("myImageInput");
  imageInput.value = canvas.toDataURL('image/png')
  form.submit();
}

camera();
document.addEventListener('click', () => {if(beforeCapture){getCurrentFrame();}else{return};});
