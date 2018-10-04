--[[
Author: Alessandro Cuppari
Language: Lua
Github: https://github.com/alessandrojcm
]]--

function cat(x)
	return x % 3 == 0
end

function bat(x)
	return x % 5 == 0
end

function spider(x)
	return bat(x) and cat(x)
end

for i = 1, 100 do
	if cat(i) then
		print('cats')
	elseif bat(i) then
		print('bats')
	elseif spider(i) then
		print('spiders')
	else
		print(i)
	end
end
