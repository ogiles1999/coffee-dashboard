from cProfile import run
import runpy

if __name__ == "__main__":
    runpy.run_module("app.main", run_name="__main__", alter_sys=True)
