program Verkauf2 (input, output);
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
	if Anzahl <= 0 then
		writeln('falsche Eingabe')
	else
	{ es liegt eine Bestellung vor }
	begin
		Preis := Anzahl * GRUNDPREIS;
		if Anzahl > 50 then
		{ ein grosser Rabatt wird erteilt }
			Preis := Preis * 0.8
		else
			if Anzahl > 10 then
			{ kleiner Rabatt gewaehrt }
				Preis := Preis * 0.9;
		writeln ('Der Preis betraegt ', Preis, ' EUR')
	end
end. { Verkauf2 }
