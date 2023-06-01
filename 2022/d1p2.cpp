#include <iostream>
#include <algorithm>

int main() {
    int** data = nullptr;  // 存储每组数据
    int* groupSums = nullptr;  // 存储每组数据的和

    int maxGroups = 0;  // 最大组数
    int maxNumbers = 0;  // 每组最大数字个数
    int maxTopSums = 0;  // 需要计算的最大和个数

    int groupCount = 0;  // 实际组数
    int currentGroupSize = 0;  // 当前组的数字个数

    // 读取用户输入的数据
    int num;
    while (std::cin >> num) {
        if (num == -1) {
            // 输入-1作为结束标志
            break;
        }
        if (num == -2) {
            // 输入-2作为组之间的分隔符
            groupSums[groupCount] = 0;
            for (int i = 0; i < currentGroupSize; ++i) {
                groupSums[groupCount] += data[groupCount][i];
            }
            groupCount++;

            // 动态增加数组大小
            if (groupCount >= maxGroups) {
                int newMaxGroups = maxGroups + 5;
                int** newData = new int*[newMaxGroups];
                int* newGroupSums = new int[newMaxGroups];

                // 复制数据
                for (int i = 0; i < maxGroups; ++i) {
                    newData[i] = data[i];
                    newGroupSums[i] = groupSums[i];
                }

                // 释放旧内存
                delete[] data;
                delete[] groupSums;

                data = newData;
                groupSums = newGroupSums;

                maxGroups = newMaxGroups;
            }

            // 重置当前组的数字个数
            currentGroupSize = 0;
        } else {
            if (currentGroupSize >= maxNumbers) {
                // 动态增加数组大小
                int newMaxNumbers = maxNumbers + 5;
                int* newData = new int[newMaxNumbers];

                // 复制数据
                for (int i = 0; i < maxNumbers; ++i) {
                    newData[i] = data[groupCount][i];
                }

                // 释放旧内存
                delete[] data[groupCount];

                data[groupCount] = newData;

                maxNumbers = newMaxNumbers;
            }

            data[groupCount][currentGroupSize] = num;
            currentGroupSize++;
        }
    }

    // 计算最后一组数据的和
    groupSums[groupCount] = 0;
    for (int i = 0; i < currentGroupSize; ++i) {
        groupSums[groupCount] += data[groupCount][i];
    }
    groupCount++;

    // 找到最大的三个和
    std::sort(groupSums, groupSums + groupCount, std::greater<int>());
    int result = 0;
    int actualTopSums = std::min(maxTopSums, groupCount);
    for (int i = 0; i < actualTopSums; ++i) {
        result += groupSums[i];
    }

    // 释放内存
    for (int i = 0; i < groupCount; ++i) {
        delete[] data[i];
    }
    delete[] data;
    delete[] groupSums;

    // 输出结果
    std::cout << "最大的" << actualTopSums << "个和之和为: " << result << std::endl;

    return 0;
}
