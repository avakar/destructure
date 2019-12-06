# Structure to Tuple Conversions in C++17

This single-header library provides the following pair of functions.

    template <typename T>
    auto destructure(T & val)
    {
        auto && [an...] = std::forward<T>(val);
        return std::tie(an...);
    }

    template <typename T>
    auto destructure(T && val)
    {
        auto && [an...] = std::forward<T>(val);
        return std::tuple(std::move(an)...);
    }

Unfortunately, there are no variadic structured bindings in C++17,
so the implementation is a bit more involved.

## Getting Started

Either use the CMakeFile in the repo or simply copy `destructure.h`
to your project. Then include it.

    #include <avakar/destructure.h>
    using avakar::destructure;

Now, consider the following structure.

    struct X
    {
        int a;
        std::string b;
    };

The `destructure` function will turn an object of type `X` into a tuple
of `int` and `std::string`.

    X x;
    auto tied = destructure(x);
    static_assert(std::is_same_v<decltype(tied), std::tuple<int &, std::string &>>);

Notice that for an l-value, destructuring results in a tuple
of references. You can modify the object `x` via the tuple.

    std::get<0>(tied) = 1;
    assert(x.a == 1);

For an r-value, `destructure` returns a tuple of values.

    auto tup = destructure(X{1, "test"});
    static_assert(std::is_same_v<decltype(tied), std::tuple<int, std::string>>);

## Limitations

The library only supports structures of up to 64 members by default,
although you can generate your own version of the header with
the following command.

    ./src/generate.py -n 100

This will output a new header file containing the function
in the `destructure_100` namespace. Use `--inline` to make the namespace
inline.
