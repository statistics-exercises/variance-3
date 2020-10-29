# Average least square deviation

The method of least squares is not the best way of deriving estimators for the parameters of random variables as there are many cases where it simply does not work (it is easy to show, for instance, that you cannot use it to derive estimators for the parameters for a binomial random variable for instance).  As we will see in later parts of the SOR1020 course it is very useful when we have linear models.  For now, we will leave the method in order to focus on the quantity that is minimised within it, which we have thus far called the "spread":

![](https://render.githubusercontent.com/render/math?math=S^2=\frac{1}{n}\sum_{i=1}^{n}[X_i-\mathbb{E}(X)]^2)

__To complete this exercise I would like you to write code that generates a graph showing how this quantity changes as a function of the number of random variables that it is computed from increases.__  We will keep things simple and will sample our various ![](https://render.githubusercontent.com/render/math?math=X_i) values from a uniform distribution that is between 0 and 1 for such a distribution ![](https://render.githubusercontent.com/render/math?math=\mathhb{E}(X)=0.5).  What you are thus calculating is sample means for various different n values of the random variable ![](https://render.githubusercontent.com/render/math?math=[U(0,1)-0.5]^2).  I have written some code to get you started.  To complete the exercise you will need to:

1. Set the first element of the array called `indices` equal to 1, the second element of the array called `indices` to 2 and so on.
2. Set the first element of the array called `S2` equal to a sample mean computed using the above formula with n=1, the second element of this array to a sample mean computed using the above formula with n=2 and so up until you have computed the formula above with n=200.

When your code is complete a graph showing the value of ![](https://render.githubusercontent.com/render/math?math=S^2) as a function of n will be generated.
