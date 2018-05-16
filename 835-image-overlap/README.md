## Idea

Since there is only translation `left`, `right`, `up`, `down`,  this is exactly the same as treating `B` as `kernel` to convolve `A`, to make sure we get every convolution, the padding should be `B.shape - 1`.