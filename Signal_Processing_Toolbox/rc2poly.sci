function a = rc2poly(k)
    a = k(1)
    for i = 2 : length(k)
        a = [a + a(i-1:-1:1)*k(i) k(i)]
    end
    a = [1 a]
endfunction

a = rc2poly([0.3090 0.9800 0.0031 0.0082 -0.0082])
