import * as THREE from 'three';

const container = document.getElementById( 'canvas' )

const scene = new THREE.Scene();
scene.background = new THREE.Color(0xffffff);
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setPixelRatio( window.devicePixelRatio )
renderer.setSize( window.innerWidth, window.innerHeight );
container.appendChild( renderer.domElement );

const geometry = new THREE.BoxGeometry( 5, 1, 4 );
var cubeMaterials = [
  new THREE.MeshBasicMaterial({color:0x03045e}),
  new THREE.MeshBasicMaterial({color:0x023e8a}),
  new THREE.MeshBasicMaterial({color:0x0077b6}),
  new THREE.MeshBasicMaterial({color:0x03045e}),
  new THREE.MeshBasicMaterial({color:0x023e8a}),
  new THREE.MeshBasicMaterial({color:0x0077b6}),
];
const cube = new THREE.Mesh( geometry, cubeMaterials );
scene.add( cube );

camera.position.z = 5;

function animate() {
  requestAnimationFrame( animate );
	renderer.render( scene, camera );
}

animate();
let web_socket = new WebSocket('ws://localhost:8000')

window.addEventListener('resize', function(event) {
  renderer.setSize( window.innerWidth, window.innerHeight );
}, true);

web_socket.onmessage = function (event) {
  let json = JSON.parse(event.data)
  var keys = Object.keys(json)

  var acel_eixo_x_data = json[keys[0]]['values'][0]
  var acel_eixo_x = document.getElementsByClassName('acel_eixo_x')
  acel_eixo_x.innerHTML = `eixo X: ${acel_eixo_x_data}`
  var acel_eixo_y_data = json[keys[0]]['values'][1]
  var acel_eiyo_y = document.getElementsByClassName('acel_eixo_y')
  acel_eiyo_y.innerHTML = `eixo Y: ${acel_eixo_y_data}`
  var acel_eixo_z_data = json[keys[0]]['values'][2]
  var acel_eizo_z = document.getElementsByClassName('acel_eixo_z')
  acel_eizo_z.innerHTML = `eixo X: ${acel_eixo_z_data}`

  var giro_eixo_x_data = json[keys[1]]['values'][0]
  var giro_eixo_x = document.getElementsByClassName('giro_eixo_x')
  giro_eixo_x.innerHTML = `eixo X: ${giro_eixo_x_data}`
  var giro_eixo_y_data = json[keys[1]]['values'][1]
  var giro_eiyo_y = document.getElementsByClassName('giro_eixo_y')
  giro_eiyo_y.innerHTML = `eixo Y: ${giro_eixo_y_data}`
  var giro_eixo_z_data = json[keys[1]]['values'][2]
  var giro_eizo_z = document.getElementsByClassName('giro_eixo_z')
  giro_eizo_z.innerHTML = `eixo X: ${giro_eixo_z_data}`

  let axle_x_temp = parseFloat(giro_eixo_x_data)
  cube.rotation.x += axle_x_temp/20
  let axle_y_temp = parseFloat(giro_eixo_y_data)
  cube.rotation.y += axle_y_temp/20
  let axle_z_temp = parseFloat(giro_eixo_z_data)
  cube.rotation.z += axle_z_temp/20
}

let button_ref = document.getElementById('reset')
button_ref.onclick = function() {
  cube.rotation.x = 0
  cube.rotation.y = 0
  cube.rotation.z = 0
}
