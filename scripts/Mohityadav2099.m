%Author: Mohit Yadav
%Language: Matlab
%Github: https://github.com/Mohityadav2099

for x=1:100
    if mod(x,3)==0 && mod(x,5)==0
        disp('spiders')
    elseif mod(x,3)==0
        disp('cats')
    elseif mod(x,5)==0
        disp('bats')
    else 
        disp(x)
    end
end
