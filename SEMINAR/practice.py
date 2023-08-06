# void Towers(string with = "1", string on = "3", string some = "2", int count = 2)
# {
#     //Console.WriteLine($"1. {with}, {on}, {some}");
#     if(count > 1) Towers(with, some, on, count - 1);

#     //Console.WriteLine($"2. {with}, {on}, {some}");
#     Console.WriteLine($"{with} >> {on}");

#    // Console.WriteLine($"3. {with}, {on}, {some}");
#     if(count > 1) Towers(some, on, with, count - 1);
# }
# Towers();



