var map = L.map('map').setView([56.8519, 60.6122], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
    '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
  maxZoom: 19
}).addTo(map);

var marker = L.marker([0.0, 0.0]).addTo(map);

map.on('click', function (e) {
  marker.setLatLng(e.latlng);

  document.getElementById('id_latitude').value = e.latlng.lat.toFixed(6);
  document.getElementById('id_longitude').value = e.latlng.lng.toFixed(6);
});
