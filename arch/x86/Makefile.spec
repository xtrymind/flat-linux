# for CONFIG_OPTIMIZE_SPECIFICALLY
# gcc -march=native -E -v - </dev/null 2>&1 | grep cc1
cflags-$(CONFIG_OPTIMIZE_FOR_2500)	+= -march=sandybridge -mmmx -mno-3dnow -msse -msse2 -msse3 -mssse3 -mno-sse4a -mcx16 -msahf -mno-movbe -maes -mno-sha -mpclmul -mpopcnt -mno-abm -mno-lwp -mno-fma -mno-fma4 -mno-xop -mno-bmi -mno-sgx -mno-bmi2 -mno-pconfig -mno-wbnoinvd -mno-tbm -mavx -mno-avx2 -msse4.2 -msse4.1 -mno-lzcnt -mno-rtm -mno-hle -mno-rdrnd -mno-f16c -mno-fsgsbase -mno-rdseed -mno-prfchw -mno-adx -mfxsr -mxsave -mxsaveopt -mno-avx512f -mno-avx512er -mno-avx512cd -mno-avx512pf -mno-prefetchwt1 -mno-clflushopt -mno-xsavec -mno-xsaves -mno-avx512dq -mno-avx512bw -mno-avx512vl -mno-avx512ifma -mno-avx512vbmi -mno-avx5124fmaps -mno-avx5124vnniw -mno-clwb -mno-mwaitx -mno-clzero -mno-pku -mno-rdpid -mno-gfni -mno-shstk -mno-avx512vbmi2 -mno-avx512vnni -mno-vaes -mno-vpclmulqdq -mno-avx512bitalg -mno-movdiri -mno-movdir64b --param l1-cache-size=32 --param l1-cache-line-size=64 --param l2-cache-size=6144 -mtune=sandybridge

# from arch/x86/Makefile: Prevent GCC from generating any FP code by mistake.
cflags-$(CONFIG_OPTIMIZE_SPECIFICALLY) += -mno-sse -mno-mmx -mno-sse2 -mno-3dnow
cflags-$(CONFIG_OPTIMIZE_SPECIFICALLY) += $(call cc-option,-mno-avx,)
