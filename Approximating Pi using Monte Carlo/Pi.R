runs = 1e3 ###Number of samples
r = 1 ###Radius of circle

pi_values = c()

for (i in 1:runs) {
  x = runif(runs, -r, r)
  y = runif(runs, -r, r)
  pi_values[i] = (sum(x^2+y^2 <= r^2)/runs)*4
}

error = abs(pi-pi_values)

appx_pi = c()
for (i in 1:length(pi_values)){ ###Computing the mean value after each sample realization
  appx_pi[i] = mean(pi_values[1:i])
}

conv_error = c()
for (i in 1:length(error)){ ###Computing the error after each sample realization
  conv_error[i] = mean(error[1:i])
}