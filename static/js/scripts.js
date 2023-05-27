function eyeClick() {
  var eyeSvg = document.getElementById('eyeSvg');
  var originalImage = eyeSvg.getAttribute('data-original');
  var original2Image = eyeSvg.getAttribute('data-original2');

  var saldo = document.getElementById('saldo');

  if (eyeSvg.getAttribute('src') === original2Image) {
    eyeSvg.setAttribute('src', originalImage);
    saldo.style.display = 'inline';
  } else {
    eyeSvg.setAttribute('src', original2Image);
    saldo.style.display = 'none';
  }
}