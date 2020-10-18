x = linspace(0,10,1024);
dt = 10/1024;
tau = 0.1; %mean dwell time

y = [1:1024];
y(1) = 1;

dwell_start_time=0;
n_p_dwells=0;
n_ap_dwells=0;

total_p_time=0;
total_ap_time=0;

for a = 2:1024
    if(rand(1) < dt/tau)
        if(y(a-1) == 0)
            n_p_dwells = n_p_dwells+1;
            total_p_time = total_p_time+(x(a)-dwell_start_time);
            y(a) = 1;
        else    
            n_ap_dwells = n_ap_dwells+1;
            total_ap_time = total_ap_time+(x(a)-dwell_start_time);
            y(a) = 0;
        end
        dwell_start_time = x(a);
    else
        y(a) = y(a-1);
    end
end

plot(x,y);
ylim([-0.5,1.5]);

tau_ap = total_ap_time/n_ap_dwells;
tau_p = total_p_time/n_p_dwells;
