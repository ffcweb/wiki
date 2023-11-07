# C (programming language)
___

- c (pronounced /ˈsiː/ – like the letter c)[6] is a general-purpose computer programming language. it was created in the 1970s by dennis ritchie, and remains very widely used and influential. by design, c's features cleanly reflect the capabilities of the targeted cpus. it has found lasting use in operating systems, device drivers, and protocol stacks, but its use in application software has been decreasing.[7] c is commonly used on computer architectures that range from the largest supercomputers to the smallest microcontrollers and embedded systems.

- a successor to the programming language b, c was originally developed at bell labs by ritchie between 1972 and 1973 to construct utilities running on unix. it was applied to re-implementing the kernel of the unix operating system.[8] during the 1980s, c gradually gained popularity. it has become one of the most widely used programming languages,[9][10] with c compilers available for practically all modern computer architectures and operating systems. the book the c programming language, co-authored by the original language designer, served for many years as the de facto standard for the language.[11][12] c has been standardized since 1989 by the american national standards institute (ansi) and the international organization for standardization (iso).

- c is an imperative procedural language, supporting structured programming, lexical variable scope, and recursion, with a static type system. it was designed to be compiled to provide low-level access to memory and language constructs that map efficiently to machine instructions, all with minimal runtime support. despite its low-level capabilities, the language was designed to encourage cross-platform programming. a standards-compliant c program written with portability in mind can be compiled for a wide variety of computer platforms and operating systems with few changes to its source code.[13]

- since 2000, c has consistently ranked among the top two languages in the tiobe index, a measure of the popularity of programming languages.[14]

# overview

- dennis ritchie (right), the inventor of the c programming language, with ken thompson
  c is an imperative, procedural language in the algol tradition. it has a static type system. in c, all executable code is contained within subroutines (also called "functions", though not in the sense of functional programming). function parameters are passed by value, although arrays are passed as pointers, i.e. the address of the first item in the array. pass-by-reference is simulated in c by explicitly passing pointers to the thing being referenced.

- c program source text is free-form code. semicolons terminate statements, while curly braces are used to group statements into blocks.

- the c language also exhibits the following characteristics:

- the language has a small, fixed number of keywords, including a full set of control flow primitives: if/else, for, do/while, while, and switch. user-defined names are not distinguished from keywords by any kind of sigil.
- it has a large number of arithmetic, bitwise, and logic operators: +,+=,++,&,||, etc.
- more than one assignment may be performed in a single statement.

# functions:

- function return values can be ignored, when not needed.
- function and data pointers permit ad hoc run-time polymorphism.
- functions may not be defined within the lexical scope of other functions.
- variables may be defined within a function, with scope.
- a function may call itself, so recursion is supported.
- data typing is static, but weakly enforced; all data has a type, but implicit conversions are possible.
- user-defined (typedef) and compound types are possible.
- heterogeneous aggregate data types (struct) allow related data elements to be accessed and assigned as a unit. the contents of whole structs cannot be compared using a single built-in operator (the elements must be compared individually).
- union is a structure with overlapping members; it allows multiple data types to share the same memory location.
- array indexing is a secondary notation, defined in terms of pointer arithmetic. whole arrays cannot be assigned or compared using a single built-in operator. there is no "array" keyword in use or definition; instead, square brackets indicate arrays syntactically, for example month[11].
- enumerated types are possible with the enum keyword. they are freely interconvertible with integers.
  strings are not a distinct data type, but are conventionally implemented as null-terminated character arrays.
- low-level access to computer memory is possible by converting machine addresses to pointers.
- procedures (subroutines not returning values) are a special case of function, with an empty return type void.
- memory can be allocated to a program with calls to library routines.
- a preprocessor performs macro definition, source code file inclusion, and conditional compilation.
- there is a basic form of modularity: files can be compiled separately and linked together, with control over which functions and data objects are visible to other files via static and extern attributes.
- complex functionality such as i/o, string manipulation, and mathematical functions are consistently delegated to library routines.
- the generated code after compilation has relatively straightforward needs on the underlying platform, which makes it suitable for creating operating systems and for use in embedded systems.
- while c does not include certain features found in other languages (such as object orientation and garbage collection), these can be implemented or emulated, often through the use of external libraries (e.g., the glib object system or the boehm garbage collector).