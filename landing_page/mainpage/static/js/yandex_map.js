ymaps.ready(init);

function init () {
    var myMap = new ymaps.Map('map', {
        center: [55.7408157, 37.608925],
        zoom: 16,
        controls: []
    }, {
        searchControlProvider: 'yandex#search'
    });

    var myGeoObject = new ymaps.GeoObject({
        geometry: {
            type: "Point",
            coordinates: [55.7408157, 37.608925]
        }}, {
        iconLayout: 'default#image',
        iconImageHref: 'static/images/pin.png',
        iconImageSize: [30, 42],
    });

    myMap.geoObjects
        .add(myGeoObject);

}