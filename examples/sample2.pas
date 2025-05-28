program Sample2;

var
  a: integer;
  b: real;
  c: char;
  d: set of char;
  e: boolean;
  f: string;

begin
  a := 10;
  b := 20.5;
  c := 'x';
  d := ['a', 'b', 'c', 'd'];
  e := true;
  f := 'Hello, Pascal!';

  if a > 5 then
    write('a is greater than 5')
  else
    write('a is not greater than 5');

  write('Value of b: ', b);
  write('Character c: ', c);
  write('Boolean e: ', e);
  write('String f: ', f);

  if c in d then
    write(c, ' is in the set d')
  else
    write(c, ' is not in the set d');
end.