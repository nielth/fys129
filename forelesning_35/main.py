from pylab import *

g = 9.8 # m/s^2 tyngdealsellerasjon
time = 4. # s total tid
y0 = 57.0 #m starthøyde
v0 = 0.0# m/s start hastighet
D = 0.1 # luftmotstand
dt = 0.0001
n = int(ceil(time/dt))
# Variables
y = zeros(n)
v = zeros(n)
a = zeros(n)
t = zeros(n)


# Initialize
y[0] = y0
v[0] = v0
a[0] = -g
# Integration loop
for i in range(0,n-1):
    a[i+1] = -g -D*v[i]*abs(v[i])
    v[i+1] = v[i] + a[i]*dt
    y[i+1] = y[i] + v[i+1]*dt
    t[i+1] = t[i] + dt


#tt=arange(0,4,0.001)

figur = figure()
subplot(3,1,1)
plot(t,y)
#plot(tt,-0.5*g*tt**2+y0,'red')
xticks([])
ylabel('$y(t)$  [m]')
subplot(3,1,2)
plot(t,v)
#plot(tt,-g*tt,'red')
xticks([])
ylabel('$v(t)$  [m/s]')
subplot(3,1,3)
plot(t,a)
xlabel('$t$  [s]')
ylabel('$a(t)$  [m/s$^2$]')
show()
figur.savefig("aksellerasjon_hastighet_posisjon.pdf", bbox_inches='tight')




#plot(t,-0.5*g*t**2+y0,'red')

show()