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
  let coord = event.data.split('|')

  let axle_x_temp = parseFloat(coord[0])
  cube.rotation.x += axle_x_temp/20
  let axle_y_temp = parseFloat(coord[1])
  cube.rotation.y += axle_y_temp/20
  let axle_z_temp = parseFloat(coord[2])
  cube.rotation.z += axle_z_temp/20
}

let button_ref = document.getElementById('reset')
button_ref.onclick = function() {
  cube.rotation.x = 0
  cube.rotation.y = 0
  cube.rotation.z = 0
}
