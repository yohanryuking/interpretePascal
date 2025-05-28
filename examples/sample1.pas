program Sample1;

var
  a: integer;
  b: real;
  c: char;
  d: set of char;
  e: boolean;
  f: string;

begin
  a := 5;
  b := 3.14;
  c := 'x';
  d := ['a', 'b', 'c'];
  e := true;
  f := 'Hello, Pascal!';

  if a > 0 then
    write('a is positive')
  else
    write('a is non-positive');

  write('Value of b: ', b);
  write('Character c: ', c);
  write('Set d contains a: ', 'a' in d);
  write('Boolean e: ', e);
  write('String f: ', f);
end.