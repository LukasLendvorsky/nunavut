from pathlib import Path
import subprocess

def dsdl_compile(language :str,
                 root_namespace_directory: Path,
                 lookup_directories: list[Path],
                 output_directory: Path,
                 template_directory: Path | None = None) -> None:
    args = [
        "nnvg",
        "--target-language",
        language,
        "--outdir",
        str(output_directory),
        "--file-mode",
        "0o664",
        "--verbose",
        "--experimental-languages"
    ]
    if (template_directory is not None):
        args += ["--templates", str(template_directory)]

    for lookup_directory in lookup_directories:
        args += ["--lookup-dir", str(lookup_directory)]
    args += [str(root_namespace_directory)]

    print("Running command:", " ".join(args))

    subprocess.run(args, check=True)


dsdl_compile(
    language="py_c_python",
    root_namespace_directory=Path("../submodules/public_regulated_data_types/uavcan"),
    lookup_directories=[],
    output_directory=Path("./generated_py")
)

dsdl_compile(
    language="py_c_library",
    root_namespace_directory=Path("../submodules/public_regulated_data_types/uavcan"),
    lookup_directories=[],
    output_directory=Path("./generated_c")
)


from scikit_build_core.build import *
