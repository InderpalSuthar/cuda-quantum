def check_qutip_installed():
    try:
        import qutip
    except ImportError:
        raise ImportError("QuTiP is not installed. Install it using 'pip install qutip' to use this feature.")