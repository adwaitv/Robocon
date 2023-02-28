function [ u ] = controller(~, s, s_des, params)
%PD_CONTROLLER  PD controller for the height
%
%   s: 2x1 vector containing the current state [z; v_z]
%   s_des: 2x1 vector containing desired state [z; v_z]
%   params: robot parameters

e=s_des(1)-s(1);
e1=s_des(2)-s(2);
Kp=40;
Kd=10;
u = params.mass*(params.gravity + Kp*e + Kd*e1);

% FILL IN YOUR CODE HERE


end