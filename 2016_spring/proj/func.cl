__kernel void calc(__global int *ks, __global int **data, __global int height, __global int width, __global int **res, __private int x, __private int y)
{
    for (__private int i = max(0, y - 50); i < min(y + 51, height); i++)
        for (__private int j = max(0, x - 50); j < min(x + 51, width); j++)
            res[x][y] += (data[y][x] - 0.055) * ks[abs(i - y) + abs(j - x)];
    res[x][y] /= (min(width, j + 51) - max(j - 50, 0)) * (min(height, i + 51) -  max(i - 50, 0));
    res[x][y] *= 2;
    if (res[x][y] < 0.055)
        res[x][y] = 0;
}  

            
