#=
Author @maurxeugenio
Algoritmo de ordenação buble sort, feito em Julia [juja]
[os comentários em muitas linhas é bem mais lindo que em python.]
=#

# lista_desordenada = [10, 3, 4, 5, 6, 1, 4, 5,6, 30, 1, 500, 200]

# function odernar(lista)
#     for i in 1:length(lista)
# 		for j in 1:(length(lista) - 1)
# 			if lista[j] > lista[j+1]
# 				aux = lista[j]
# 				lista[j] = lista[j+1]
# 				lista[j+1] = aux
# 			end
# 		end
# 	end
# 	return lista
# end

for i = 1:100
    if i % 3 == 0
        if i % 5 == 0
            println("Spiders")
        end
        println("cats")
    elseif i % 5 == 0
        println("bats")
    end
    println(i)

end

# print(odernar(lista_desordenada))
