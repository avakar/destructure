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

## Limitations

The library only supports structures of up to 64 members by default,
although you can generate your own version of the header with
the follwing command.

    ./tools/generate.py -n 100

This will output a new header file containing the function
in the `destructure_100` namespace. Use `--inline` to make the namespace
inline.