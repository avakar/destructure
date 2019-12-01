#include <avakar/destructure.h>
#include <memory>
#include <optional>
#include <string>
#include <type_traits>
#include <utility>
using namespace avakar;

struct empty {};

template <typename T>
struct singleton
{
	T t;
};

struct many
{
	int a;
	std::string b;
	std::optional<char> c;
};

int main()
{
	static_assert(std::is_same_v<decltype(destructure(empty{})), std::tuple<>>);

#define X(A, ...) static_assert(std::is_same_v<decltype(destructure(std::declval<A>())), std::tuple<__VA_ARGS__>>)

	X(singleton<int>, int);
	X(singleton<const int>, const int);
	X(singleton<std::unique_ptr<int>>, std::unique_ptr<int>);
	X(many, int, std::string, std::optional<char>);

	X(singleton<int> &, int &);
	X(singleton<const int> &, const int &);
	X(singleton<std::unique_ptr<int>> &, std::unique_ptr<int> &);
	X(many &, int &, std::string &, std::optional<char> &);

	return 0;
}
