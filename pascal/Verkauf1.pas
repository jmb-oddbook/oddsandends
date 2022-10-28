program Verkauf1 (input, output);
{ Rabattgewaehrung }

	const
	GRUNDPREIS = 200.00 {EUR};
	
	var
	Anzahl : integer;
	Preis : real;
	
begin
	writeln ('Bitte die Anzahl bestellter Waren ',
			 'eingeben:');
	readln (Anzahl);
	if Anzahl > 0 then
	{ es liegt eine Bestellung vor }
	begin
		Preis := Anzahl * GRUNDPREIS;
		if Anzahl > 10 then
		{ ein Rabatt wird erteilt }
			if Anzahl > 50 then
			{ grosser Rabatt gewaehrt }
				Preis := Preis * 0.8
			else
			{ kleiner Rabatt gewaehrt }
				Preis := Preis * 0.9;
		writeln ('Der Preis betraegt ', Preis, ' EUR')
	end
	else
		writeln ('falsche Eingabe')
end. { Verkauf1 }
