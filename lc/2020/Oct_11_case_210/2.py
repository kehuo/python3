# @File: 2
# @Author: Kevin Huo
# @LastUpdate: 10/11/2020 10:23 AM

from collections import defaultdict
from typing import List


class Solution(object):



#
#
# class Solution(object):
#     def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
#         """
#         https://leetcode-cn.com/contest/weekly-contest-210/problems/maximal-network-rank/
#         todo - test[2]超时
#         """
#         if n == 2:
#             return 1 if roads else 0
#         # d = defaultdict(lambda: 0)
#         d = defaultdict(set)
#         for u,v in roads:
#             d[u].add(v)
#             d[v].add(u)
#         # d= {2: {3}, 3: {0, 2}, 0: {3, 4}, 4: {0, 1}, 1: {4}}
#         # list(d) = [2, 3, 0, 4, 1]
#         print("d= %s" % dict(d))
#         print("list d = %s" % list(d))
#         order = list(d)
#         order.sort(key=lambda x: len(d[x]), reverse=True)
#         print("order: %s" % order)
#         # print("d= %s" % dict(d))
#         res = 0
#         for i in range(n):
#             for j in range(n):
#                 if i == j:
#                     continue
#                 curr_zhi = d[i] + d[j]
#                 if ([i, j] in roads) or ([j, i] in roads):
#                     curr_zhi -= 1
#                 # print("i=%s, j=%s, zhi=%s" % (i, j, curr_zhi))
#                 res = max(res, curr_zhi)
#         print(res)
#         return res
#

if __name__ == '__main__':
    # ans = [4, 4, 超时]
    tests = [
        [5, [[2, 3], [0, 3], [0, 4], [4, 1]]],
        [4, [[0, 1], [0, 3], [1, 2], [1, 3]]],
        [99,
         [[45, 37], [57, 50], [94, 78], [58, 12], [59, 96], [42, 23], [49, 78], [89, 91], [79, 4], [15, 81], [70, 18],
          [9, 46], [98, 16], [43, 92], [70, 43], [88, 8], [24, 40], [31, 24], [15, 55], [28, 41], [34, 70], [36, 49],
          [59, 63], [72, 61], [52, 81], [58, 32], [29, 13], [11, 25], [79, 95], [62, 37], [9, 25], [2, 7], [10, 62],
          [71, 73], [55, 46], [85, 56], [78, 66], [22, 8], [73, 28], [23, 97], [54, 53], [20, 15], [40, 30], [61, 36],
          [63, 32], [66, 8], [21, 72], [29, 43], [50, 63], [8, 85], [7, 69], [35, 94], [52, 38], [89, 10], [69, 12],
          [89, 85], [13, 1], [3, 33], [91, 31], [23, 78], [84, 7], [84, 4], [68, 49], [5, 89], [16, 84], [97, 82],
          [86, 38], [98, 86], [46, 56], [19, 33], [8, 76], [33, 24], [9, 10], [5, 52], [89, 44], [93, 66], [94, 90],
          [52, 73], [7, 51], [23, 59], [84, 63], [66, 83], [57, 77], [2, 32], [31, 36], [80, 66], [37, 74], [3, 15],
          [92, 93], [18, 31], [97, 14], [64, 2], [25, 88], [14, 71], [46, 11], [83, 31], [49, 7], [12, 73], [26, 30],
          [27, 52], [23, 24], [66, 33], [21, 30], [63, 20], [85, 13], [47, 27], [64, 59], [71, 33], [59, 48], [14, 38],
          [90, 66], [31, 85], [10, 64], [12, 60], [69, 41], [63, 74], [49, 74], [96, 19], [15, 84], [94, 38], [84, 91],
          [50, 34], [71, 26], [59, 51], [83, 60], [80, 53], [48, 93], [73, 41], [69, 25], [90, 57], [33, 12], [66, 65],
          [6, 58], [77, 94], [92, 20], [61, 48], [12, 86], [18, 23], [20, 85], [87, 7], [41, 97], [17, 78], [55, 89],
          [11, 51], [53, 66], [90, 13], [36, 64], [55, 98], [62, 26], [6, 55], [4, 27], [96, 69], [91, 67], [49, 89],
          [38, 81], [5, 28], [96, 94], [98, 47], [57, 21], [77, 51], [12, 95], [39, 77], [3, 50], [36, 96], [77, 0],
          [50, 98], [59, 1], [20, 0], [28, 71], [49, 12], [74, 9], [55, 51], [72, 7], [11, 2], [87, 46], [22, 83],
          [83, 63], [84, 29], [38, 54], [98, 87], [81, 6], [96, 64], [39, 94], [69, 49], [32, 74], [31, 63], [33, 96],
          [94, 85], [61, 58], [76, 58], [11, 22], [92, 17], [1, 8], [18, 21], [47, 26], [86, 58], [19, 54], [66, 94],
          [66, 10], [30, 10], [1, 45], [33, 21], [92, 26], [16, 24], [52, 51], [88, 66], [62, 85], [37, 98], [86, 65],
          [82, 31], [31, 10], [88, 12], [20, 69], [98, 90], [62, 18], [1, 79], [92, 28], [41, 7], [28, 25], [49, 57],
          [78, 92], [59, 95], [70, 78], [38, 68], [49, 54], [67, 39], [34, 93], [38, 53], [67, 63], [27, 26], [66, 30],
          [63, 49], [65, 1], [74, 82], [83, 19], [69, 95], [58, 36], [64, 73], [60, 39], [15, 34], [44, 37], [2, 63],
          [80, 11], [86, 1], [91, 45], [31, 30], [54, 24], [13, 61], [29, 57], [1, 49], [40, 39], [91, 50], [5, 67],
          [74, 35], [52, 0], [14, 10], [7, 5], [39, 1], [62, 54], [16, 14], [12, 3], [72, 79], [4, 94], [19, 86],
          [83, 69], [84, 85], [90, 43], [42, 48], [16, 18], [65, 27], [64, 74], [9, 65], [23, 69], [53, 48], [50, 36],
          [73, 81], [6, 65], [68, 4], [27, 19], [3, 26], [92, 94], [91, 15], [64, 78], [83, 11], [25, 4], [71, 83],
          [83, 82], [5, 92], [72, 46], [77, 5], [16, 7], [95, 90], [69, 36], [41, 92], [27, 67], [38, 72], [48, 49],
          [21, 61], [90, 58], [34, 88], [62, 91], [8, 64], [78, 45], [29, 34], [73, 30], [50, 77], [96, 2], [36, 78],
          [89, 94], [50, 22], [81, 50], [78, 18], [93, 88], [33, 18], [25, 58], [24, 71], [60, 72], [36, 25], [53, 49],
          [18, 66], [79, 11], [32, 13], [85, 97], [10, 78], [24, 69], [78, 91], [33, 94], [52, 26], [87, 75], [53, 47],
          [71, 76], [61, 97], [75, 24], [66, 3], [35, 76], [48, 76], [68, 76], [54, 7], [60, 6], [41, 48], [3, 78],
          [0, 80], [42, 27], [84, 54], [27, 82], [37, 11], [69, 44], [62, 19], [7, 3], [77, 65], [8, 56], [34, 25],
          [50, 70], [19, 73], [31, 43], [28, 21], [44, 67], [82, 50], [80, 15], [2, 0], [18, 75], [18, 58], [59, 92],
          [44, 68], [96, 34], [19, 17], [80, 23], [7, 58], [54, 75], [40, 56], [35, 26], [71, 59], [7, 89], [12, 96],
          [35, 40], [27, 31], [86, 60], [38, 85], [16, 96], [51, 23], [16, 71], [52, 39], [34, 75], [32, 93], [2, 51],
          [3, 71], [70, 64], [77, 35], [55, 56], [34, 31], [87, 96], [60, 96], [14, 72], [29, 90], [49, 66], [3, 72],
          [23, 47], [42, 61], [19, 29], [56, 45], [38, 29], [32, 78], [85, 21], [9, 79], [4, 22], [35, 16], [29, 7],
          [79, 10], [28, 40], [48, 88], [60, 91], [48, 58], [55, 1], [83, 90], [88, 80], [89, 66], [47, 89], [53, 24],
          [73, 48], [89, 82], [47, 48], [44, 36], [98, 71], [75, 88], [88, 23], [97, 69], [76, 61], [71, 88], [31, 66],
          [53, 74], [56, 42], [83, 3], [65, 85], [1, 74], [91, 46], [9, 82], [72, 18], [80, 62], [12, 59], [93, 11],
          [26, 43], [74, 98], [15, 69], [22, 49], [70, 14], [41, 14], [36, 34], [77, 29], [85, 34], [11, 72], [42, 28],
          [54, 83], [75, 59], [61, 16], [18, 30], [15, 64], [2, 74], [83, 16], [68, 88], [25, 76], [72, 57], [25, 37],
          [12, 23], [96, 92], [72, 43], [61, 27], [0, 62], [46, 89], [47, 90], [41, 6], [73, 60], [33, 4], [15, 89],
          [22, 41], [55, 14], [5, 51], [71, 79], [37, 8], [78, 68], [49, 71], [84, 45], [32, 39], [5, 18], [84, 66],
          [19, 77], [36, 93], [6, 63], [50, 58], [65, 73], [80, 28], [67, 77], [53, 90], [64, 16], [56, 76], [54, 94],
          [38, 47], [86, 52], [67, 56], [58, 41], [94, 37], [49, 23], [35, 2], [35, 65], [80, 27], [95, 22], [61, 7],
          [13, 42], [21, 34], [68, 75], [11, 45], [65, 44], [44, 84], [73, 78], [20, 11], [80, 59], [87, 44], [39, 33],
          [19, 8], [22, 38], [73, 5], [54, 69], [86, 84], [56, 51], [7, 94], [75, 78], [58, 79], [62, 55], [20, 48],
          [93, 42], [61, 1], [45, 32], [42, 73], [48, 77], [28, 26], [18, 38], [84, 19], [13, 66], [14, 66], [86, 32],
          [94, 80], [50, 43], [8, 32], [59, 53], [22, 94], [84, 18], [81, 91], [52, 57], [13, 84], [53, 3], [27, 11],
          [21, 82], [44, 25], [16, 86], [55, 2], [77, 36], [13, 51], [3, 69], [54, 34], [28, 59], [98, 80], [71, 46],
          [95, 10], [41, 50], [45, 74], [81, 92], [5, 46], [76, 78], [10, 20], [13, 45], [75, 46], [72, 30], [8, 29],
          [23, 40], [64, 63], [56, 29], [77, 7], [3, 25], [88, 40], [58, 56], [87, 21], [56, 70], [85, 32], [24, 89],
          [6, 11], [92, 62], [59, 36], [8, 44], [35, 60], [45, 10], [40, 63], [32, 70], [33, 42], [1, 34], [16, 89],
          [48, 63], [11, 63], [30, 24], [45, 53], [81, 21], [69, 89], [80, 87], [96, 25], [33, 47], [46, 59], [65, 52],
          [56, 72], [38, 6], [52, 94], [75, 82], [1, 77], [17, 43], [41, 27], [54, 58], [53, 4], [29, 83], [83, 75],
          [13, 72], [26, 13], [83, 52], [17, 83], [9, 97], [96, 75], [29, 1], [73, 80], [88, 91], [59, 93], [9, 96],
          [12, 42], [62, 67], [53, 84], [71, 45], [17, 45], [63, 26], [33, 48], [98, 17], [69, 75], [3, 8], [18, 14],
          [49, 98], [30, 94], [90, 81], [45, 65], [44, 76], [46, 19], [42, 69], [56, 19], [87, 51], [35, 34], [14, 95],
          [28, 69], [94, 98], [68, 50], [67, 53], [61, 96], [4, 59], [53, 27], [63, 13], [2, 80], [75, 43], [97, 88],
          [37, 96], [27, 16], [97, 75], [9, 71], [28, 22], [38, 39], [22, 5], [25, 18], [34, 67], [29, 79], [48, 90],
          [48, 82], [15, 66], [72, 4], [18, 9], [54, 23], [94, 29], [74, 13], [74, 79], [8, 71], [44, 21], [23, 62],
          [56, 94], [20, 21], [26, 45], [12, 5], [57, 28], [69, 40], [28, 67], [3, 56], [45, 63], [32, 15], [46, 44],
          [64, 93], [22, 87], [23, 15], [47, 9], [80, 95], [46, 58], [32, 40], [12, 6], [12, 4], [18, 24], [84, 6],
          [77, 38], [23, 36], [77, 55], [87, 58], [26, 66], [63, 78], [44, 29], [2, 1], [66, 23], [11, 81], [41, 71],
          [51, 8], [82, 58], [2, 38], [7, 65], [75, 86], [86, 18], [11, 9], [39, 34], [14, 93], [16, 60], [3, 0],
          [27, 25], [76, 23], [6, 16], [39, 72], [93, 98], [34, 16], [52, 40], [68, 46], [29, 20], [19, 89], [72, 95],
          [65, 14], [6, 30], [35, 32], [18, 89], [7, 82], [33, 92], [30, 0], [88, 53], [95, 3], [37, 91], [93, 53],
          [98, 78], [86, 88], [51, 49], [94, 20], [39, 88], [55, 3], [59, 49], [44, 22], [22, 30], [41, 81], [35, 91],
          [17, 3], [47, 75], [39, 10], [34, 63], [19, 48], [13, 76], [93, 50], [81, 4], [3, 96], [75, 73], [11, 4],
          [88, 82], [12, 47], [71, 87], [4, 92], [55, 38], [14, 75], [37, 56], [70, 57], [82, 77], [90, 70], [0, 59],
          [51, 28], [6, 96], [30, 65], [89, 53], [49, 77], [51, 94], [91, 42], [55, 79], [67, 15], [64, 0], [38, 71],
          [92, 9], [72, 50], [93, 0], [74, 33], [54, 89], [59, 24], [17, 10], [10, 98], [83, 85], [60, 62], [30, 36],
          [92, 75], [12, 18], [38, 78], [87, 65], [71, 69], [27, 14], [67, 92], [13, 69], [60, 22], [38, 13], [58, 43],
          [40, 16], [91, 68], [90, 23], [35, 20], [74, 90], [2, 87], [27, 35], [2, 47], [53, 14], [64, 44], [17, 21],
          [82, 39], [6, 72], [35, 86], [97, 71], [80, 74], [88, 55], [44, 14], [48, 13], [31, 7], [7, 92], [38, 45],
          [22, 58], [60, 76], [36, 47], [91, 38], [36, 37], [20, 49], [34, 56], [32, 6], [71, 44], [84, 41], [95, 4],
          [6, 34], [84, 78], [0, 55], [54, 60], [13, 91], [48, 72], [86, 46], [0, 43], [16, 93], [80, 77], [23, 96],
          [95, 65], [18, 8], [72, 15], [22, 24], [61, 30], [39, 24], [56, 17], [24, 62], [56, 83], [42, 14], [16, 94],
          [62, 90], [50, 85], [70, 94], [61, 77], [56, 62], [8, 24], [60, 7], [17, 94], [38, 40], [32, 36], [60, 33],
          [68, 58], [2, 6], [50, 42], [62, 70], [82, 30], [64, 60], [79, 70], [3, 54], [88, 92], [9, 3], [0, 37],
          [29, 75], [43, 45], [84, 17], [79, 3], [44, 81], [49, 61], [98, 85], [52, 31], [90, 72], [14, 23], [6, 88],
          [33, 14], [70, 49], [98, 68], [73, 4], [46, 33], [31, 98], [84, 32], [25, 12], [83, 46], [0, 5], [27, 12],
          [36, 1], [74, 3], [38, 34], [93, 4], [81, 97], [32, 18], [76, 40], [23, 89], [94, 3], [24, 85], [41, 43],
          [15, 27], [48, 55], [0, 40], [10, 29], [93, 94], [12, 40], [18, 11], [12, 0], [8, 10], [95, 29], [75, 17],
          [58, 91], [67, 4], [39, 90], [38, 51], [34, 22], [34, 45], [77, 24], [63, 91], [76, 28], [14, 28], [75, 64],
          [53, 18], [59, 79], [8, 33], [78, 7], [39, 7], [6, 86], [96, 62], [97, 22], [19, 68], [1, 14], [29, 28],
          [78, 30], [98, 66], [40, 93], [57, 94], [19, 74], [71, 21], [6, 87], [21, 49], [64, 14], [43, 76], [69, 19],
          [52, 70], [3, 91], [32, 97], [44, 80], [90, 61], [83, 95], [91, 54], [58, 42], [73, 37], [94, 58], [58, 30],
          [37, 63], [3, 11], [13, 35], [57, 1], [30, 27], [88, 76], [65, 24], [56, 21], [39, 71], [37, 47], [70, 76],
          [65, 58], [79, 51], [11, 14], [46, 51], [96, 17], [13, 17], [82, 45], [93, 38], [65, 41], [29, 37], [9, 8],
          [26, 98], [2, 31], [37, 21], [41, 20], [34, 41], [82, 72], [57, 79], [92, 13], [79, 22], [13, 27], [45, 76],
          [20, 75], [26, 82], [33, 57], [74, 71], [28, 75], [89, 96], [74, 92], [17, 29], [35, 75], [87, 31], [34, 4],
          [22, 66], [14, 51], [47, 88], [40, 21], [85, 27], [27, 51], [61, 11], [19, 35], [86, 93], [39, 8], [32, 21],
          [47, 76], [35, 90], [53, 58], [79, 48], [31, 28], [69, 26], [37, 60], [22, 77], [40, 36], [1, 92], [3, 35],
          [20, 7], [14, 19], [7, 38], [33, 23], [18, 45], [28, 37], [80, 57], [87, 55], [5, 32], [76, 27], [60, 51],
          [86, 76], [8, 43], [13, 34], [20, 32], [61, 29], [31, 78], [88, 17], [85, 86], [95, 30], [37, 82], [69, 60],
          [57, 22], [81, 70], [46, 66], [96, 44], [6, 94], [97, 40], [93, 30], [20, 97], [68, 14], [4, 37], [41, 51],
          [77, 27], [47, 45], [17, 36], [59, 39], [65, 5], [30, 85], [58, 88], [57, 78], [48, 85], [80, 60], [84, 74],
          [36, 71], [24, 64], [84, 38], [47, 59], [90, 52], [61, 19], [8, 69], [1, 15], [81, 94], [56, 87], [13, 8],
          [19, 57], [45, 24], [53, 44], [92, 36], [45, 20], [65, 46], [64, 81], [70, 22], [23, 32], [92, 66], [85, 53],
          [40, 42], [65, 17], [27, 3], [55, 60], [31, 53], [72, 28], [95, 54], [8, 50], [43, 69], [62, 79], [82, 17],
          [1, 20], [83, 6], [15, 92], [75, 62], [71, 58], [79, 73], [92, 27], [34, 94], [49, 30], [32, 3], [91, 33],
          [16, 90], [9, 72], [21, 41], [8, 72], [40, 79], [3, 63], [70, 91], [21, 48], [45, 14], [91, 82], [50, 79],
          [24, 52], [59, 42], [21, 15], [34, 77], [39, 97], [16, 33], [10, 50], [58, 21], [25, 54], [51, 15], [26, 50],
          [79, 20], [9, 95], [85, 87], [45, 86], [0, 79], [47, 93], [97, 19], [26, 12], [53, 7], [81, 60], [89, 8],
          [16, 12], [85, 51], [94, 97], [86, 17], [8, 55], [5, 31], [6, 26], [21, 8], [27, 55], [11, 54], [96, 11],
          [5, 70], [87, 17], [72, 78], [29, 66], [96, 26], [43, 22], [8, 73], [46, 36], [81, 33], [39, 92], [69, 35],
          [21, 52], [62, 83], [94, 61], [1, 47], [30, 55], [10, 51], [98, 95], [0, 11], [48, 57], [46, 6], [30, 1],
          [60, 28], [5, 74], [43, 42], [39, 66], [64, 42], [54, 33], [6, 14], [30, 74], [79, 24], [27, 7], [1, 98],
          [67, 47], [27, 28], [34, 87], [63, 46], [28, 0], [46, 69], [91, 64], [76, 73], [79, 89], [72, 55], [49, 9],
          [22, 46], [19, 38], [62, 74], [96, 32], [83, 39], [80, 70], [72, 85], [10, 65], [40, 49], [93, 61], [80, 89],
          [18, 91], [24, 61], [93, 44], [44, 61], [45, 36], [55, 50], [63, 30], [77, 9], [83, 40], [39, 56], [87, 77],
          [43, 25], [50, 62], [8, 86], [43, 80], [74, 72], [84, 75], [9, 26], [37, 52], [2, 71], [33, 5], [82, 8],
          [54, 52], [22, 13], [29, 65], [63, 77], [20, 47], [12, 51], [19, 11], [97, 72], [87, 86], [63, 69], [81, 96],
          [53, 26], [86, 92], [27, 22], [76, 54], [83, 61], [38, 3], [34, 55], [90, 92], [20, 44], [19, 31], [18, 67],
          [50, 76], [12, 98], [63, 55], [83, 68], [49, 87], [93, 95], [4, 96], [49, 0], [64, 66], [0, 74], [41, 77],
          [72, 96], [93, 37], [36, 86], [43, 38], [25, 41], [31, 50], [2, 57], [30, 4], [53, 29], [26, 10], [82, 10],
          [91, 87], [61, 98], [49, 32], [85, 37], [31, 47], [61, 35], [54, 28], [58, 81], [19, 85], [94, 27], [94, 26],
          [14, 17], [55, 59], [95, 42], [51, 66], [19, 80], [75, 39], [56, 22], [56, 5], [54, 68], [9, 84], [82, 42],
          [92, 47], [91, 17], [53, 40], [9, 76], [36, 66], [45, 9], [9, 36], [77, 40], [26, 36], [52, 47], [54, 37],
          [56, 61], [82, 65], [2, 95], [34, 72], [36, 52], [70, 83], [61, 52], [94, 49], [68, 25], [3, 16], [35, 5],
          [85, 41], [54, 73], [44, 1], [53, 55], [5, 47], [45, 48], [34, 46], [35, 8], [0, 32], [95, 40], [34, 60],
          [81, 67], [43, 96], [63, 33], [30, 52], [57, 45], [78, 89], [70, 4], [27, 40], [25, 15], [19, 76], [43, 5],
          [9, 31], [95, 74], [82, 56], [9, 1], [47, 16], [71, 35], [24, 13], [77, 98], [34, 95], [15, 28], [22, 51],
          [16, 1], [75, 56], [54, 51], [8, 63], [54, 17], [74, 25], [68, 28], [45, 67], [80, 58], [70, 1], [19, 71],
          [34, 43], [77, 2], [20, 14], [98, 48], [14, 74], [90, 46], [7, 40], [91, 95], [27, 96], [69, 82], [53, 5],
          [54, 20], [11, 70], [76, 42], [48, 52], [81, 79], [2, 98], [94, 41], [40, 66], [2, 65], [24, 15], [93, 28],
          [13, 50], [7, 88], [38, 95], [67, 6], [86, 72], [42, 8], [54, 35], [24, 49], [9, 98], [23, 21], [67, 64],
          [27, 48], [30, 86], [2, 13], [50, 73], [30, 35], [49, 84], [81, 45], [47, 44], [90, 44], [14, 79], [35, 36],
          [72, 0], [25, 71], [44, 17], [42, 74], [80, 36], [54, 18], [53, 71], [32, 53], [21, 36], [67, 95], [55, 74],
          [58, 45], [96, 54], [19, 87], [17, 34], [32, 34], [18, 55], [12, 79], [61, 89], [73, 6], [62, 39], [95, 41],
          [5, 54], [79, 39], [48, 30], [98, 54], [54, 32], [56, 54], [75, 27], [69, 58], [27, 10], [50, 38], [41, 11],
          [81, 27], [45, 88], [61, 67], [94, 75], [94, 72], [35, 82], [38, 58], [78, 1], [38, 69], [63, 98], [75, 53],
          [9, 38], [37, 81], [5, 75], [56, 97], [4, 16], [90, 25], [96, 13], [84, 0], [54, 93], [61, 3], [22, 32],
          [28, 48], [86, 27], [35, 73], [8, 49], [39, 78], [3, 4], [53, 15], [64, 34], [7, 46], [0, 96], [23, 2],
          [9, 13], [90, 87], [97, 29], [61, 17], [46, 77], [42, 2], [87, 88], [51, 40], [90, 54], [4, 71], [41, 89],
          [5, 29], [28, 84], [31, 51], [87, 81], [28, 78], [26, 14], [90, 73], [87, 50], [10, 85], [28, 97], [58, 19],
          [70, 30], [14, 0], [53, 34], [71, 93], [84, 81], [27, 59], [29, 87], [32, 41], [15, 83], [15, 76], [1, 54],
          [98, 57], [0, 60], [31, 22], [3, 30], [13, 43], [52, 45], [47, 39], [11, 10], [41, 86], [40, 57], [37, 95],
          [36, 48], [52, 63], [12, 37], [98, 83], [46, 32], [20, 57], [15, 11], [53, 2], [55, 54], [67, 75], [43, 66],
          [98, 51], [50, 28], [35, 41], [55, 73], [51, 43], [61, 91], [37, 83], [75, 41], [6, 97], [76, 14], [29, 51],
          [56, 20], [88, 20], [78, 90], [67, 17], [42, 46], [64, 79], [10, 13], [62, 11], [24, 6], [34, 0], [43, 91],
          [70, 71], [88, 10], [40, 54], [12, 91], [29, 22], [35, 84], [24, 27], [68, 35], [93, 29], [59, 85], [87, 60],
          [44, 79], [88, 50], [89, 59], [53, 37], [57, 83], [20, 42], [72, 54], [93, 9], [96, 67], [76, 77], [89, 88],
          [20, 74], [17, 26], [12, 53], [29, 0], [65, 79], [8, 47], [32, 71], [40, 60], [48, 50], [60, 92], [98, 23],
          [69, 29], [29, 80], [87, 15], [85, 82], [26, 74], [61, 31], [63, 89], [86, 13], [73, 36], [73, 93], [29, 55],
          [65, 90], [28, 61], [68, 93], [69, 47], [77, 33], [66, 67], [67, 49], [84, 40], [47, 95], [47, 22], [30, 43],
          [94, 32], [1, 60], [10, 33], [1, 89], [44, 7], [92, 31], [72, 66], [43, 19], [78, 11], [74, 56], [32, 75],
          [57, 73], [35, 79], [97, 57], [13, 64], [71, 1], [0, 95], [44, 55], [97, 15], [40, 61], [59, 67], [65, 96],
          [0, 23], [44, 41], [77, 52], [12, 76], [19, 10], [9, 20], [38, 56], [33, 97], [39, 35], [46, 28], [90, 5],
          [85, 79], [87, 14], [43, 62], [5, 78], [87, 53], [10, 52], [75, 80], [33, 31], [63, 19], [60, 52], [59, 17],
          [33, 56], [81, 63], [69, 88], [51, 71], [16, 28], [77, 30], [56, 23], [30, 75], [68, 66], [55, 78], [47, 50],
          [13, 6], [81, 69], [54, 81], [60, 56], [30, 62], [38, 67], [22, 37], [41, 64], [62, 82], [66, 37], [72, 16],
          [80, 20], [76, 0], [97, 66], [95, 50], [42, 97], [44, 52], [36, 72], [24, 11], [90, 15], [29, 86], [16, 56],
          [92, 8], [2, 40], [24, 28], [86, 64], [11, 30], [66, 62], [30, 91], [36, 8], [27, 64], [39, 13], [44, 56],
          [9, 62], [1, 75], [49, 16], [79, 52], [33, 69], [17, 71], [59, 26], [19, 53], [65, 57], [87, 33], [86, 83],
          [26, 2], [30, 81], [25, 53], [20, 87], [95, 87], [40, 44], [82, 15], [41, 46], [51, 20], [52, 96], [57, 38],
          [89, 74], [70, 85], [84, 69], [71, 6], [38, 1], [89, 67], [85, 57], [37, 51], [24, 80], [23, 20], [21, 96],
          [93, 6], [81, 86], [86, 63], [81, 43], [22, 39], [75, 61], [38, 80], [52, 35], [96, 56], [11, 56], [59, 78],
          [80, 3], [87, 23], [25, 60], [82, 19], [9, 15], [52, 2], [94, 83], [53, 61], [91, 65], [63, 35], [13, 68],
          [83, 5], [54, 66], [27, 83], [59, 19], [18, 2], [69, 70], [19, 7], [50, 30], [72, 42], [47, 4], [22, 92],
          [36, 81], [35, 18], [93, 8], [40, 18], [63, 27], [83, 42], [84, 8], [27, 20], [80, 52], [68, 70], [46, 47],
          [24, 83], [90, 51], [67, 70], [85, 26], [63, 22], [4, 23], [35, 46], [72, 52], [51, 24], [62, 59], [33, 30],
          [93, 60], [95, 13], [82, 38], [83, 45], [73, 96], [57, 47], [34, 37], [85, 68], [37, 2], [29, 12], [67, 84],
          [63, 70], [62, 38], [93, 27], [68, 7], [46, 92], [40, 6], [71, 75], [71, 30], [64, 95], [83, 53], [91, 11],
          [70, 54], [54, 9], [19, 93], [6, 10], [91, 55], [1, 33], [16, 70], [70, 93], [30, 98], [41, 83], [11, 66],
          [93, 17], [46, 24], [63, 82], [22, 2], [71, 40], [24, 2], [52, 91], [9, 59], [81, 16], [79, 69], [98, 82],
          [12, 87], [59, 33], [40, 22], [44, 19], [63, 56], [82, 59], [65, 25], [55, 13], [2, 33], [73, 21], [5, 82],
          [93, 3], [44, 6], [95, 62], [95, 92], [16, 20], [42, 89], [69, 85], [50, 52], [61, 14], [77, 88], [72, 91],
          [92, 61], [75, 15], [34, 74], [81, 23], [80, 4], [34, 3], [29, 35], [61, 88], [51, 93], [47, 63], [76, 90],
          [12, 34], [42, 80], [80, 67], [26, 44], [13, 62], [23, 13], [22, 71], [97, 59], [31, 77], [58, 8], [8, 60],
          [83, 84], [61, 59], [27, 98], [33, 78], [48, 38], [70, 66], [24, 87], [4, 29], [20, 50], [86, 5], [26, 54],
          [66, 82], [74, 83], [88, 9], [90, 8], [97, 12], [91, 75], [14, 89], [45, 35], [84, 42], [10, 90], [89, 60],
          [49, 2], [53, 79], [54, 6], [23, 34], [24, 19], [79, 25], [40, 37], [75, 93], [41, 49], [86, 74], [81, 5],
          [0, 21], [98, 4], [34, 79], [95, 15], [52, 41], [97, 60], [10, 25], [57, 5], [22, 84], [6, 80], [17, 0],
          [87, 38], [81, 42], [77, 72], [45, 62], [79, 26], [70, 44], [83, 65], [72, 70], [56, 52], [58, 10], [7, 0],
          [86, 50], [89, 29], [36, 5], [22, 98], [79, 86], [91, 2], [15, 70], [50, 90], [79, 49], [45, 29], [57, 14],
          [51, 91], [94, 65], [66, 21], [3, 28], [17, 66], [68, 61], [49, 47], [94, 79], [63, 93], [45, 79], [87, 10],
          [57, 71], [17, 80], [68, 36], [42, 94], [97, 10], [25, 13], [48, 71], [44, 85], [7, 93], [54, 50], [57, 41],
          [58, 16], [52, 92], [69, 94], [22, 81], [0, 70], [60, 26], [44, 23], [61, 22], [52, 71], [81, 59], [91, 66],
          [79, 93], [37, 32], [75, 85], [81, 32], [45, 80], [6, 22], [55, 97], [34, 81], [14, 94], [24, 97], [22, 55],
          [86, 73], [52, 15], [61, 37], [27, 87], [68, 65], [53, 77], [8, 4], [0, 90], [88, 33], [76, 93], [72, 29],
          [93, 31], [57, 92], [81, 35], [27, 29], [25, 73], [6, 98], [72, 37], [78, 62], [86, 2], [28, 1], [29, 50],
          [58, 23], [91, 36], [9, 17], [48, 17], [9, 78], [32, 31], [47, 3], [97, 52], [81, 55], [26, 64], [8, 52],
          [30, 20], [52, 55], [5, 49], [86, 3], [93, 84], [3, 6], [84, 65], [83, 58], [70, 23], [0, 85], [17, 74],
          [65, 12], [78, 29], [78, 27], [73, 72], [40, 5], [17, 6], [24, 60], [83, 59], [30, 87], [20, 86], [72, 2],
          [12, 81], [18, 50], [64, 43], [30, 16], [24, 74], [56, 91], [82, 36], [83, 20], [45, 94], [30, 13], [45, 12],
          [44, 16], [73, 26], [22, 68], [66, 50], [59, 65], [76, 32], [15, 42], [8, 28], [34, 83], [51, 67], [51, 53],
          [4, 78], [47, 10], [74, 46], [60, 29], [77, 14], [22, 48], [79, 66], [64, 32], [77, 75], [77, 60], [27, 8],
          [96, 49], [23, 30], [20, 12], [54, 41], [35, 12], [33, 32], [25, 29], [11, 92], [25, 32], [63, 42], [41, 39],
          [39, 12], [17, 35], [50, 44], [91, 28], [18, 46], [62, 81], [90, 75], [29, 33], [67, 48], [88, 90], [91, 93],
          [17, 79], [92, 10], [55, 67], [98, 75], [98, 29], [37, 17], [82, 13], [38, 32], [1, 21], [57, 66], [76, 75],
          [74, 48], [36, 62], [11, 49], [22, 14], [57, 24], [90, 12], [45, 40], [24, 21], [66, 96], [47, 61], [86, 51],
          [80, 14], [52, 28], [1, 80], [61, 12], [15, 44], [10, 49], [80, 63], [92, 56], [19, 5], [80, 5], [7, 56],
          [59, 8], [32, 67], [20, 13], [81, 85], [60, 57], [16, 97], [34, 30], [88, 22], [5, 37], [53, 56], [10, 4],
          [93, 78], [61, 85], [33, 26], [91, 40], [29, 39], [48, 78], [89, 64], [5, 4], [88, 57], [10, 1], [58, 51],
          [59, 60], [64, 5], [79, 19], [20, 62], [40, 55], [35, 96], [23, 9], [90, 69], [5, 66], [10, 23], [37, 68],
          [90, 49], [44, 33], [82, 86], [47, 66], [67, 23], [6, 91], [15, 86], [42, 75], [5, 21], [70, 19], [93, 45],
          [91, 57], [20, 55], [53, 94], [90, 14], [62, 16], [50, 40], [68, 97], [52, 87], [7, 17], [45, 55], [92, 85],
          [72, 22], [2, 16], [64, 54], [27, 1], [87, 63], [13, 0], [65, 60], [94, 46], [68, 59], [97, 31], [85, 1],
          [59, 35], [13, 46], [58, 47], [1, 97], [8, 65], [88, 26], [60, 95], [1, 66], [4, 82], [14, 25], [0, 1],
          [85, 45], [52, 46], [15, 94], [2, 89], [94, 95], [35, 85], [56, 81], [70, 6], [83, 50], [86, 71], [86, 34],
          [28, 19], [22, 45], [28, 32], [61, 32], [75, 12], [62, 27], [17, 31], [11, 39], [36, 15], [77, 73], [27, 32],
          [0, 91], [41, 79], [78, 37], [73, 16], [72, 88], [90, 96], [41, 47], [42, 29], [52, 3], [89, 21], [97, 45],
          [83, 67], [12, 7], [9, 21], [24, 98], [55, 68], [25, 52], [41, 55], [87, 1], [33, 22], [6, 75], [76, 30],
          [65, 47], [45, 95], [62, 41], [84, 52], [22, 67], [90, 6], [64, 35], [25, 31], [69, 18], [27, 5], [52, 11],
          [31, 26], [96, 20], [85, 5], [95, 33], [49, 39], [13, 67], [52, 82], [27, 84], [95, 66], [69, 86], [23, 71],
          [40, 25], [10, 44], [65, 32], [87, 18], [17, 57], [69, 67], [8, 53], [83, 72], [30, 38], [10, 53], [56, 59],
          [94, 2], [73, 15], [34, 71], [4, 83], [85, 74], [68, 51], [26, 91], [29, 40], [72, 67], [72, 31], [96, 88],
          [87, 61], [67, 57], [23, 68], [4, 62], [21, 51], [90, 26], [78, 53], [95, 82], [10, 36], [65, 23], [34, 19],
          [2, 5], [30, 57], [98, 25], [64, 3], [79, 91], [6, 95], [9, 86], [9, 89], [12, 21], [31, 71], [18, 76],
          [75, 95], [40, 82], [92, 18], [34, 26], [79, 7], [73, 1], [18, 82], [41, 87], [29, 54], [15, 16], [69, 93],
          [54, 0], [78, 71], [56, 88], [55, 84], [94, 21], [69, 73], [63, 15], [24, 47], [24, 55], [46, 53], [37, 39],
          [38, 26], [32, 29], [76, 3], [16, 95], [45, 51], [41, 53], [97, 74], [27, 49], [19, 32], [39, 63], [88, 60],
          [8, 25], [81, 51], [65, 13], [84, 79], [84, 33], [0, 9], [64, 83], [74, 7], [37, 46], [45, 3], [65, 37],
          [56, 28], [10, 24], [70, 39], [34, 47], [60, 32], [67, 10], [18, 98], [3, 75], [86, 22], [44, 78], [33, 65],
          [31, 21], [56, 68], [17, 38], [95, 56], [63, 14], [39, 27], [76, 74], [50, 23], [30, 60], [87, 59], [51, 83],
          [5, 39], [24, 29], [47, 7], [24, 91], [15, 8], [17, 68], [81, 0], [36, 24], [70, 92], [15, 22], [60, 85],
          [58, 78], [35, 21], [36, 95], [63, 24], [9, 61], [54, 39], [10, 34], [2, 73], [48, 44], [71, 13], [84, 43],
          [70, 9], [1, 3], [16, 50], [78, 15], [58, 74], [88, 29], [48, 66], [56, 98], [10, 22], [62, 53], [74, 73],
          [55, 4], [74, 28], [2, 50], [39, 16], [43, 63], [68, 60], [44, 24], [76, 52], [75, 89], [50, 9], [84, 96],
          [45, 69], [26, 87], [20, 39], [13, 18], [38, 37], [67, 1], [82, 11], [68, 45], [15, 93], [29, 49], [88, 54],
          [67, 37], [25, 49], [8, 75], [59, 57], [97, 30], [59, 22], [75, 51], [90, 7], [70, 59], [11, 34], [46, 60],
          [46, 81], [93, 49], [88, 16], [67, 94], [84, 47], [86, 57], [22, 1], [16, 65], [87, 73], [16, 92], [27, 50],
          [17, 46], [70, 29], [4, 65], [43, 21], [10, 38], [56, 14], [84, 98], [89, 12], [33, 64], [26, 23], [39, 68],
          [88, 32], [92, 0], [4, 87], [42, 34], [71, 10], [50, 84], [16, 74], [95, 61], [26, 56], [40, 43], [33, 55],
          [77, 42], [14, 30], [25, 48], [91, 97], [41, 63], [40, 80], [59, 29], [71, 65], [53, 76], [54, 67], [16, 11],
          [55, 95], [39, 2], [58, 34], [61, 70], [23, 84], [46, 76], [14, 31], [47, 81], [34, 73], [16, 59], [46, 95],
          [53, 28], [84, 2], [48, 18], [8, 5], [78, 86], [27, 91], [41, 31], [17, 70], [87, 45], [90, 89], [72, 10],
          [10, 48], [80, 55], [37, 69], [74, 57], [13, 4], [55, 42], [87, 5], [43, 2], [15, 7], [43, 88], [42, 32],
          [60, 66], [14, 58], [39, 95], [45, 70], [21, 83], [20, 70], [89, 72], [92, 80], [85, 4], [97, 18], [82, 94],
          [22, 52], [98, 45], [82, 41], [35, 58], [8, 0], [47, 42], [92, 24], [11, 73], [67, 12], [71, 96], [96, 45],
          [1, 69], [46, 84], [13, 40], [80, 41], [89, 4], [64, 84], [81, 28], [74, 8], [30, 12], [63, 44], [6, 5],
          [11, 58], [33, 11], [61, 51], [57, 54], [48, 81], [79, 54], [65, 63], [55, 65], [92, 2], [33, 51], [5, 93],
          [20, 90], [78, 40], [78, 50], [39, 43], [53, 97], [68, 43], [42, 79], [3, 18], [12, 63], [85, 25], [51, 76],
          [30, 28], [23, 92], [86, 42], [86, 53], [43, 47], [76, 91], [66, 38], [95, 1], [42, 26], [38, 25], [20, 38],
          [91, 19], [78, 85], [44, 94], [79, 68], [86, 23], [73, 10], [98, 35], [95, 18], [42, 17], [75, 10], [50, 89],
          [84, 30], [73, 61], [95, 57], [36, 88], [12, 43], [0, 57], [57, 27], [82, 87], [92, 12], [78, 81], [18, 51],
          [19, 42], [24, 41], [47, 14], [77, 58], [46, 39], [8, 11], [6, 33], [15, 18], [27, 0], [33, 9], [90, 56],
          [79, 61], [83, 78], [34, 44], [5, 26], [85, 96], [70, 74], [27, 95], [97, 35], [34, 92], [51, 26], [42, 10],
          [11, 26], [74, 59], [11, 97], [38, 46], [26, 22], [17, 47], [23, 82], [9, 83], [69, 21], [85, 80], [41, 59],
          [6, 76], [10, 35], [31, 58], [52, 18], [60, 79], [49, 6], [80, 50], [41, 5], [65, 39], [97, 49], [72, 87],
          [85, 77], [13, 79], [60, 61], [21, 16], [17, 76], [18, 22], [28, 49], [15, 39], [49, 81], [46, 43], [75, 79],
          [20, 34], [27, 33], [98, 72], [92, 32], [97, 98], [39, 3], [74, 22], [41, 37], [35, 88], [30, 67], [30, 89],
          [18, 61], [34, 18], [49, 83], [64, 80], [10, 41], [75, 11], [57, 4], [78, 74], [3, 48], [93, 72], [16, 46],
          [43, 52], [13, 78], [37, 9], [9, 51], [72, 49], [73, 32], [12, 38], [33, 34], [78, 35], [36, 13], [58, 93],
          [79, 36], [56, 69], [29, 14], [20, 72], [36, 4], [55, 66], [59, 31], [9, 91], [0, 42], [62, 6], [54, 42],
          [36, 3], [51, 47], [38, 15], [43, 77], [6, 15], [62, 28], [49, 64], [29, 92], [10, 86], [49, 37], [4, 35],
          [48, 7], [73, 29], [82, 71], [92, 87], [62, 97], [53, 60], [84, 10], [26, 16], [10, 68], [52, 29], [24, 66],
          [22, 7], [57, 13], [97, 76], [18, 68], [58, 96], [97, 34], [73, 51], [42, 87], [41, 60], [78, 88], [98, 0],
          [44, 42], [76, 92], [44, 62], [18, 65], [70, 21], [25, 77], [69, 17], [19, 9], [92, 77], [65, 76], [78, 54],
          [79, 43], [84, 59], [8, 17], [11, 35], [15, 37], [36, 76], [68, 5], [77, 20], [53, 11], [32, 7], [40, 3],
          [88, 2], [29, 26], [60, 14], [10, 32], [63, 1], [35, 23], [27, 45], [64, 56], [43, 10], [56, 49], [40, 62],
          [29, 91], [24, 93], [87, 40], [70, 28], [97, 89], [40, 72], [11, 74], [64, 88], [68, 29], [23, 16], [38, 98],
          [40, 34], [87, 16], [98, 96], [21, 14], [93, 52], [74, 96], [29, 46], [84, 95], [50, 39], [50, 71], [36, 56],
          [97, 70], [82, 70], [50, 65], [88, 1], [76, 21], [16, 53], [6, 52], [20, 3], [92, 45], [2, 70], [65, 48],
          [91, 98], [58, 17], [80, 10], [80, 34], [61, 38], [40, 48], [24, 50], [23, 57], [53, 91], [46, 21], [51, 30],
          [55, 61], [55, 69], [88, 98], [55, 16], [62, 12], [78, 12], [68, 47], [62, 48], [24, 7], [80, 61], [9, 4],
          [18, 43], [86, 48], [98, 41], [89, 65], [25, 91], [68, 67], [56, 1], [2, 29], [76, 22], [37, 18], [90, 77],
          [73, 31], [64, 12], [7, 30], [74, 66], [66, 6], [64, 11], [4, 46], [45, 33], [12, 66], [13, 58], [49, 42],
          [59, 11], [62, 2], [78, 51], [80, 21], [70, 25], [94, 31], [63, 16], [74, 31], [44, 27], [3, 88], [57, 12],
          [15, 65], [97, 58], [5, 16], [79, 30], [31, 40], [18, 0], [98, 65], [57, 82], [9, 43], [70, 33], [8, 57],
          [95, 81], [39, 26], [53, 35], [57, 18], [92, 55], [7, 64], [6, 61], [49, 91], [52, 66], [80, 91], [18, 6],
          [95, 20], [82, 0], [41, 42], [39, 9], [82, 84], [20, 93], [85, 42], [44, 95], [28, 13], [98, 7], [63, 79],
          [62, 73], [93, 65], [90, 17], [11, 38], [32, 57], [31, 45], [78, 20], [1, 41], [55, 11], [95, 23], [46, 2],
          [78, 21], [74, 12], [12, 85], [17, 32], [51, 19], [48, 37], [80, 72], [13, 60], [36, 54], [95, 58], [53, 20],
          [1, 50], [42, 67], [20, 81], [47, 18], [33, 0], [14, 49], [0, 25], [53, 30], [7, 73], [74, 77], [34, 91],
          [34, 28], [83, 43], [48, 14], [82, 43], [78, 77], [95, 96], [65, 19], [26, 67], [75, 40], [34, 76], [96, 40],
          [62, 98], [6, 56], [48, 75], [89, 20], [42, 66], [95, 31], [85, 91], [66, 77], [63, 72], [52, 59], [17, 16],
          [55, 76], [9, 69], [41, 72], [62, 89], [81, 14], [28, 55], [43, 98], [85, 63], [39, 98], [4, 45], [3, 19],
          [55, 71], [58, 63], [37, 42], [98, 33], [73, 45], [13, 77], [36, 41], [5, 30], [81, 29], [17, 50], [6, 28],
          [59, 20], [96, 70], [73, 89], [6, 39], [4, 44], [4, 15], [87, 64], [48, 70], [11, 13], [49, 58], [33, 72],
          [49, 86], [36, 83], [20, 26], [68, 3], [92, 72], [71, 56], [66, 59], [23, 28], [1, 62], [39, 31], [65, 22],
          [6, 69], [7, 63], [49, 46], [62, 76], [14, 46], [9, 63], [40, 9], [15, 50], [36, 63], [65, 34], [30, 68],
          [28, 44], [22, 9], [70, 13], [28, 7], [36, 55], [11, 84], [54, 27], [66, 75], [40, 70], [36, 16], [23, 6],
          [81, 24], [52, 89], [66, 61], [96, 55], [87, 25], [73, 59], [50, 64], [72, 32], [86, 31], [24, 86], [45, 2],
          [11, 40], [18, 73], [91, 92], [18, 29], [65, 21], [23, 79], [67, 7], [15, 14], [14, 88], [63, 54], [51, 6],
          [41, 15], [92, 83], [91, 41], [21, 64], [38, 42], [91, 48], [21, 53], [10, 74], [35, 72], [25, 17], [18, 17],
          [6, 47], [64, 72], [46, 50], [50, 5], [70, 88], [44, 98], [98, 40], [33, 85], [3, 10], [19, 55]]]
    ]
    t = tests[0]

    s = Solution()
    s.maximalNetworkRank(*t)
