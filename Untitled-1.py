% greedy algorithm(GA)贪心/贪婪算法

%购入了 numBottles 瓶酒
print(num_bottles = input('please input the number of bottles:'));
%用 numExchange 个空酒瓶可以兑换一瓶新酒
print(num_exchange = input('please input the number of exchange:'));

%初始化
sumb = num_bottles;  % 喝到酒的数目
empty = num_bottles;  % 空瓶数目

%贪心：当前喝完所有饮料后变为空瓶加上已有空瓶后，最大限度的、贪心的兑换饮料，依次类推，
% 直到手上的空瓶不足以兑换出一瓶饮料止。

while fix(empty / num_exchange) ~= 0 
    % fix函数用于取整数商，表示当前空瓶还能兑换酒时：进入循环；否则不足以兑换酒：循环退出
    bottle = fix(empty / num_exchange);  % 利用当前空瓶最大限度地兑换酒，得到当前酒的数目
    sumb = sumb + bottle;  % 更新喝到酒的数目
    empty = mod(empty,num_exchange) + bottle; %更新空瓶数目:空瓶=兑换后剩余空瓶+兑换得到的酒瓶
end


sumb %最终喝到酒的瓶数

