import sys


class GraduationCeremony:

    def __init__(self, n):
        self.n = n

    def solution(self):
        n = self.n
        m = 4
        dp = [1] * (m + 1)
        dp[m] = 0

        for i in range(1, n + 1):
            temp = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                temp[j] = dp[0] + dp[j + 1]

            temp, dp = dp, temp

        x1 = dp[0]  # total number of valid way to attend classes
        x2 = temp[1]  # total number of way to miss last day

        return f"{x2}/{x1}"


if __name__ == "__main__":
    try:
        days = int(sys.argv[1])
    except IndexError:
        print("Please pass 'days' argument in command line")
    except ValueError:
        print("'Days' argument must be of integer type")
    except Exception as e:
        print(e)
    gc = GraduationCeremony(days)
    print(gc.solution())
