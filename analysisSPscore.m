%%% ECE 208
%%% Analysis FastSP
%%% This program reads the FastSP result then plots them.


close all
data = xlsread('result.xls');
group = data(:,1);
p = data(:,2);
ere = data(:, 3);
B = data(:, 4);
SP_score = data(:, 5);
spfn = data(:, 6);
spfp = data(:, 7);

x = 34:5:84;


% default backbone

figure(1)
hold on;
color = ['b','r','k'];
c = 1;
for p_val = [0.5, 0.75, 0.875]
    
    p = data(:,2);
    B = data(:, 4);
    idx = (B==0 & p==p_val);
    group = data(idx,1);
    ere = data(idx, 3);
    SP_score = data(idx, 5);

    count = zeros(1, length(x));
    y = zeros(1, length(x));
    for i = 1:length(SP_score)

        idx = find(x==ere(i));
        count(idx) = count(idx)+1;
        y(idx) = y(idx) + SP_score(i);
    end
    
    y = y./count;
    opt = [color(c),'*'];
    y_fit = fit((x/100)',y', 'poly1')
    plot(x/100, y,opt,'LineWidth',2,'MarkerSize',10)
    plot(x/100, y_fit(x/100),[color(c)] ,'LineWidth',2)
    c = c+1;
end

legend('0.5', '0.5-fit', '0.75','0.75-fit', '0.875', '0.875-fit')
xlabel('ere')
ylabel('Error')
set(gca,'FontSize',15);
% change backbone

figure(2)
subplot(2,2,1)
hold on;

x = 64:5:84;
color = ['r','b', 'k','m']
% p = 0.5, B=500-4000
for i = 0:3
    y = data(7+i:4:23+i,5);
    c = [color(i+1),'*-'];
    plot(x/100,y,c,'LineWidth',2)
end
   
xlabel('Group 50%')
ylabel('Erroe')
text(0.62,0.5,'(a)','FontSize',15)
set(gca,'FontSize',15);
axis([0.6 0.85 0 0.6])
subplot(2,2,2)
hold on;

% p = 0.75
for i = 0:3
    y = data(33+i:4:52+i,5);
    c = [color(i+1),'o:'];
    plot(x/100,y,c,'LineWidth',2)
end
xlabel('Group 75%')
ylabel('Erroe')
set(gca,'FontSize',15);
text(0.62,0.5,'(b)','FontSize',15)
axis([0.6 0.85 0 0.6])
subplot(2,2,3)
hold on;

for i = 0:3
    y = data(59+i:4:78+i,5);
    c = [color(i+1),'p--'];
    plot(x/100,y,c,'LineWidth',2)
end
text(0.62,0.5,'(c)','FontSize',15)
axis([0.6 0.85 0 0.6])
xlabel('Group 87.5%')
ylabel('Erroe')
set(gca,'FontSize',15);

subplot(2,2,4)
hold on;
x = [0.5, 0.75, 0.875];
rt1 = [23.2, 13.45, 3.6];
rt2 = [13.82, 7.82, 1.79];
rt3 = [11, 3.7, 1.67];
rt4 = [10, 5.77, 1.67];
plot(x, rt1, 'rx-','LineWidth',2, 'MarkerSize', 10)
plot(x, rt2, 'b*-','LineWidth',2, 'MarkerSize', 10)
plot(x, rt3, 'kp-','LineWidth',2, 'MarkerSize', 10)
plot(x, rt4, 'm^-','LineWidth',2, 'MarkerSize', 10)

xlabel('Length Percentage')
ylabel('Running Time(min)')

text(0.85,24,'(d)','FontSize',15)
axis([0.4 0.9 0 25])
set(gca,'FontSize',15);