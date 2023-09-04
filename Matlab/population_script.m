% population control problem with crops, deer, and bear. Crops are eaten by deer and deer are eaten by bear.

% Experiment 1: No PID - comment out FSM, set u(i) = 0
% Experiment 2: PID with reference 22
% Experiment 3: Change PID reference to 10
% Experiment 4: Change r to 0.8 in population_model file
% Experiment 5: Uncomment time loop below

clear
clc
close all

T = 200;
Nvalue = 1000;     
deltavalue = T/Nvalue;   

% yout3(1) will be crops
% yout3(2) will be deer
% yout3(3) will be bear
N = Nvalue;
delta = deltavalue;
tout3 = zeros(N+1,1);
yout3 = zeros(N+1,4);
u = zeros(N+1,1);
t = 0;
crop_pop = 50;
deer_pop = 20;
bear_pop = 15;
yout3(1,1) = crop_pop;
yout3(1,2) = deer_pop;
yout3(1,3) = bear_pop;

% PID
kp = 0.452;
ki = 0.007;
kd = 0.1;

% PID Initializations
previous_error = 0;
integral = 0;
u(1) = 0;

% reference deer
deer_control = 22;

for i = 2:N+1;
        
    % FSM 
    if (deer_pop > 22)
        error = deer_control - deer_pop;
        integral = integral + error*delta;
        derivative = (error-previous_error)/delta;
        u(i) = kp*error + ki*integral + kd*derivative;
        previous_error = error;
    else
         u(i) = 0;
   end
   if u(i) > 0
        u(i) = 0; % restriction that PID cannot be greater than zero
   end
   
   % Uncomment below to see results of drought experiment
%    if t > 25 && t <26
%        crop_pop = .1*crop_pop;
%    end
   
    [tout_temp, yout_temp] = ode45(@population_model, [0 delta], [crop_pop deer_pop bear_pop u(i)]);
    
    crop_pop = yout_temp(end,1);
    deer_pop = yout_temp(end,2);
    bear_pop = yout_temp(end,3);
    t = t + delta;
    tout3(i) = t;
    yout3(i,1) = crop_pop;
    yout3(i,2) = deer_pop;
    yout3(i,3) = bear_pop;
    
end

% Plot for populations
figure('Name','Figure 1','NumberTitle','off');
plot(tout3, yout3(:,1), 'r-', tout3, yout3(:,2), 'b-',tout3,yout3(:,3),'g-')
grid
xlabel('Time (t)')
ylabel('Population')
legend('Crops','Deer','Bear')
title('Predator-Prey Model with Omnivore')

% plot for inputs
figure('Name','Figure 2','NumberTitle','off');
plot(tout3,u(:,1),'r-')
grid
xlabel('Time (t)')
ylabel('u')
title('Input')
