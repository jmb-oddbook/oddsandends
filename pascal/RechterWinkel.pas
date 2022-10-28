program RechterWinkel (input, output);
{ Pruefung ob ein Dreieck einen rechten Winkel besitzt. }

	var
	x,
	y,
	z : integer;
	r : boolean;

begin
	{ lese und drucke Dreiecksseiten }
	writeln ('Drei Seitenlaengen eingeben:');
	readln (x);
	readln (y);
	readln (z);
	writeln (x:3, y:3, z:3);
	
	if (x*x = (y*y + z*z)) or (y*y = (x*x + z*z)) or (z*z = (x*x + y*y)) then
		r := true
	else
		r := false;
	
	writeln(r)
	{ writeln('Die eingebenen Seitenlaegen bilden ein rechtwinkliges',
			' Dreieck: ', r) }
end. { RechterWinkel }
