
function [ydot] = population_model2(t,x)
% Constants
a1 = 3.2;
a2 = 2;
b1 = 0.6;
b2 = 0.36;
c1 = 75;
c2 = 50;
d = 0.56;
k = 150;
r = 1.6; 

% inputs
crops = x(1); % number of crops initially
deer = x(2); % number of deer initially
bear = x(3); % number of bear initially
u = x(4); % PID input

ydot = zeros(4,1);
ydot(1) = r*crops*(1-crops/k)-a1*crops*deer/(c1+crops)-a2*crops*bear/(c1+crops);
ydot(2) = b1*a1*crops*deer/(c1+crops)-d*deer;
ydot(3) = b1*a1*crops*bear/(c1+crops)-d*bear;
ydot(4) = 0;

% ydot(1) = (r+u)*crops*(1-crops/k)-a*crops*deer/(c+crops)-a*crops*bear/(c+crops);
% ydot(2) = b*a*crops*deer/(c+crops)-d*deer;
% ydot(3) = b*a*crops*bear/(c+crops)-d*bear;
% ydot(4) = 0;
% h = x(1); % number of hares initially
% l = x(2); % number of lynx initially
% u = x(3); % amount of hare food
% 
% ydot = zeros(2,1);
% ydot(1) = (r+u)*h*(1-h/k)-a*h*l/(c+h);
% ydot(2) = b*a*h*l/(c+h)-d*l;
% ydot(3) = 0;

end
