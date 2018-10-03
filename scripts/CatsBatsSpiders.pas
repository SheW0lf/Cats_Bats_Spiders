// AUTHOR: Damian Dabrowski
// LANGUAGE: Pascal
// GITHUB: https://github.com/ddcodepl

Program CatsBatsSpiders(output);
var i : integer;

begin
    for i := 1 to 100 do
    begin
        if ((i mod 3) = 0)
        then
            begin
                if ((i mod 5) = 0)
                    then writeln('Spiders')
                    else writeln('Cats');
            end
        else if ((i mod 5) = 0)
            then writeln('Bats')
            else writeln(i);
    end;
end.
