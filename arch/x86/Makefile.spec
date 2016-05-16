# for CONFIG_OPTIMIZE_SPECIFICALLY
# gcc -march=native -E -v - </dev/null 2>&1 | grep cc1

# from arch/x86/Makefile: Prevent GCC from generating any FP code by mistake.
cflags-$(CONFIG_OPTIMIZE_SPECIFICALLY) += -mno-sse -mno-mmx -mno-sse2 -mno-3dnow
cflags-$(CONFIG_OPTIMIZE_SPECIFICALLY) += $(call cc-option,-mno-avx,)
