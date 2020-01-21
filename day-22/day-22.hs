import Data.Modular

lineToTransform ("deal":"into":"new":"stack":xs)   = (-1, -1)
lineToTransform ("cut":x:xs)                       = (1, -(read x :: Integer))
lineToTransform ("deal":"with":"increment":x:xs)   = ((read x :: Integer), 0)

affine         m (c0, c1) (t0, t1) = ((t0 * c0) `mod` m, (t0 * c1 + t1) `mod` m)
shuffles = map(lineToTransform . words)
shuffled m = foldl (affine m)

main = do
  input <- getContents
  print $ shuffled 10007 (1, 2019) $ shuffles $ lines input
