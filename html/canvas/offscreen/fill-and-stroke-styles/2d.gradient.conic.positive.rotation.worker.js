// DO NOT EDIT! This test has been generated by /html/canvas/tools/gentest.py.
// OffscreenCanvas test in a worker:2d.gradient.conic.positive.rotation
// Description:Conic gradient with positive rotation
// Note:

importScripts("/resources/testharness.js");
importScripts("/html/canvas/resources/canvas-tests.js");

var t = async_test("Conic gradient with positive rotation");
var t_pass = t.done.bind(t);
var t_fail = t.step_func(function(reason) {
    throw reason;
});
t.step(function() {

var canvas = new OffscreenCanvas(100, 50);
var ctx = canvas.getContext('2d');

const g = ctx.createConicGradient(3*Math.PI/2, 50, 25);
// It's red in the upper right region and green on the lower left region
g.addColorStop(0, "#f00");
g.addColorStop(0.25, "#0f0");
g.addColorStop(0.50, "#0f0");
g.addColorStop(0.75, "#f00");
ctx.fillStyle = g;
ctx.fillRect(0, 0, 100, 50);
_assertPixelApprox(canvas, 25,15, 255,0,0,255, "25,15", "255,0,0,255", 3);
_assertPixelApprox(canvas, 75,40, 0,255,0,255, "75,40", "0,255,0,255", 3);
t.done();

});
done();
