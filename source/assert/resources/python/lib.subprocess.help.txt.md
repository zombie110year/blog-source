[Origin-File](/assert/repos/python/lib.subprocess.help.txt)

Help on module subprocess:

NAME
    subprocess - Subprocesses with accessible I/O streams

DESCRIPTION
    This module allows you to spawn processes, connect to their
    input/output/error pipes, and obtain their return codes.
    
    For a complete description of this module see the Python documentation.
    
    Main API
    ========
    run(...): Runs a command, waits for it to complete, then returns a
              CompletedProcess instance.
    Popen(...): A class for flexibly executing a command in a new process
    
    Constants
    ---------
    DEVNULL: Special value that indicates that os.devnull should be used
    PIPE:    Special value that indicates a pipe should be created
    STDOUT:  Special value that indicates that stderr should go to stdout
    
    
    Older API
    =========
    call(...): Runs a command, waits for it to complete, then returns
        the return code.
    check_call(...): Same as call() but raises CalledProcessError()
        if return code is not 0
    check_output(...): Same as check_call() but returns the contents of
        stdout instead of a return code
    getoutput(...): Runs a command in the shell, waits for it to complete,
        then returns the output
    getstatusoutput(...): Runs a command in the shell, waits for it to complete,
        then returns a (exitcode, output) tuple

CLASSES
    builtins.Exception(builtins.BaseException)
        SubprocessError
            CalledProcessError
            TimeoutExpired
    builtins.object
        CompletedProcess
        Popen
        STARTUPINFO
    
    class CalledProcessError(SubprocessError)
     |  Raised when run() is called with check=True and the process
     |  returns a non-zero exit status.
     |  
     |  Attributes:
     |    cmd, returncode, stdout, stderr, output
     |  
     |  Method resolution order:
     |      CalledProcessError
     |      SubprocessError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, returncode, cmd, output=None, stderr=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __str__(self)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  stdout
     |      Alias for output attribute, to match stderr
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from SubprocessError:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class CompletedProcess(builtins.object)
     |  A process that has finished running.
     |  
     |  This is returned by run().
     |  
     |  Attributes:
     |    args: The list or str args passed to run().
     |    returncode: The exit code of the process, negative for signals.
     |    stdout: The standard output (None if not captured).
     |    stderr: The standard error (None if not captured).
     |  
     |  Methods defined here:
     |  
     |  __init__(self, args, returncode, stdout=None, stderr=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  check_returncode(self)
     |      Raise CalledProcessError if the exit code is non-zero.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Popen(builtins.object)
     |  Execute a child program in a new process.
     |  
     |  For a complete description of the arguments see the Python documentation.
     |  
     |  Arguments:
     |    args: A string, or a sequence of program arguments.
     |  
     |    bufsize: supplied as the buffering argument to the open() function when
     |        creating the stdin/stdout/stderr pipe file objects
     |  
     |    executable: A replacement program to execute.
     |  
     |    stdin, stdout and stderr: These specify the executed programs' standard
     |        input, standard output and standard error file handles, respectively.
     |  
     |    preexec_fn: (POSIX only) An object to be called in the child process
     |        just before the child is executed.
     |  
     |    close_fds: Controls closing or inheriting of file descriptors.
     |  
     |    shell: If true, the command will be executed through the shell.
     |  
     |    cwd: Sets the current directory before the child is executed.
     |  
     |    env: Defines the environment variables for the new process.
     |  
     |    universal_newlines: If true, use universal line endings for file
     |        objects stdin, stdout and stderr.
     |  
     |    startupinfo and creationflags (Windows only)
     |  
     |    restore_signals (POSIX only)
     |  
     |    start_new_session (POSIX only)
     |  
     |    pass_fds (POSIX only)
     |  
     |    encoding and errors: Text mode encoding and error handling to use for
     |        file objects stdin, stdout and stderr.
     |  
     |  Attributes:
     |      stdin, stdout, stderr, pid, returncode
     |  
     |  Methods defined here:
     |  
     |  __del__(self, _maxsize=9223372036854775807, _warn=<built-in function warn>)
     |  
     |  __enter__(self)
     |  
     |  __exit__(self, type, value, traceback)
     |  
     |  __init__(self, args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=<object object at 0x00000285D0F6B110>, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0, restore_signals=True, start_new_session=False, pass_fds=(), *, encoding=None, errors=None)
     |      Create new Popen instance.
     |  
     |  communicate(self, input=None, timeout=None)
     |      Interact with process: Send data to stdin.  Read data from
     |      stdout and stderr, until end-of-file is reached.  Wait for
     |      process to terminate.
     |      
     |      The optional "input" argument should be data to be sent to the
     |      child process (if self.universal_newlines is True, this should
     |      be a string; if it is False, "input" should be bytes), or
     |      None, if no data should be sent to the child.
     |      
     |      communicate() returns a tuple (stdout, stderr).  These will be
     |      bytes or, if self.universal_newlines was True, a string.
     |  
     |  kill = terminate(self)
     |  
     |  poll(self)
     |      Check if child process has terminated. Set and return returncode
     |      attribute.
     |  
     |  send_signal(self, sig)
     |      Send a signal to the process.
     |  
     |  terminate(self)
     |      Terminates the process.
     |  
     |  wait(self, timeout=None, endtime=None)
     |      Wait for child process to terminate.  Returns returncode
     |      attribute.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class STARTUPINFO(builtins.object)
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  dwFlags = 0
     |  
     |  hStdError = None
     |  
     |  hStdInput = None
     |  
     |  hStdOutput = None
     |  
     |  wShowWindow = 0
    
    class SubprocessError(builtins.Exception)
     |  Common base class for all non-exit exceptions.
     |  
     |  Method resolution order:
     |      SubprocessError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class TimeoutExpired(SubprocessError)
     |  This exception is raised when the timeout expires while waiting for a
     |  child process.
     |  
     |  Attributes:
     |      cmd, output, stdout, stderr, timeout
     |  
     |  Method resolution order:
     |      TimeoutExpired
     |      SubprocessError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, cmd, timeout, output=None, stderr=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __str__(self)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  stdout
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from SubprocessError:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args

FUNCTIONS
    call(*popenargs, timeout=None, **kwargs)
        Run command with arguments.  Wait for command to complete or
        timeout, then return the returncode attribute.
        
        The arguments are the same as for the Popen constructor.  Example:
        
        retcode = call(["ls", "-l"])
    
    check_call(*popenargs, **kwargs)
        Run command with arguments.  Wait for command to complete.  If
        the exit code was zero then return, otherwise raise
        CalledProcessError.  The CalledProcessError object will have the
        return code in the returncode attribute.
        
        The arguments are the same as for the call function.  Example:
        
        check_call(["ls", "-l"])
    
    check_output(*popenargs, timeout=None, **kwargs)
        Run command with arguments and return its output.
        
        If the exit code was non-zero it raises a CalledProcessError.  The
        CalledProcessError object will have the return code in the returncode
        attribute and output in the output attribute.
        
        The arguments are the same as for the Popen constructor.  Example:
        
        >>> check_output(["ls", "-l", "/dev/null"])
        b'crw-rw-rw- 1 root root 1, 3 Oct 18  2007 /dev/null\n'
        
        The stdout argument is not allowed as it is used internally.
        To capture standard error in the result, use stderr=STDOUT.
        
        >>> check_output(["/bin/sh", "-c",
        ...               "ls -l non_existent_file ; exit 0"],
        ...              stderr=STDOUT)
        b'ls: non_existent_file: No such file or directory\n'
        
        There is an additional optional argument, "input", allowing you to
        pass a string to the subprocess's stdin.  If you use this argument
        you may not also use the Popen constructor's "stdin" argument, as
        it too will be used internally.  Example:
        
        >>> check_output(["sed", "-e", "s/foo/bar/"],
        ...              input=b"when in the course of fooman events\n")
        b'when in the course of barman events\n'
        
        If universal_newlines=True is passed, the "input" argument must be a
        string and the return value will be a string rather than bytes.
    
    getoutput(cmd)
        Return output (stdout or stderr) of executing cmd in a shell.
        
        Like getstatusoutput(), except the exit status is ignored and the return
        value is a string containing the command's output.  Example:
        
        >>> import subprocess
        >>> subprocess.getoutput('ls /bin/ls')
        '/bin/ls'
    
    getstatusoutput(cmd)
        Return (exitcode, output) of executing cmd in a shell.
        
        Execute the string 'cmd' in a shell with 'check_output' and
        return a 2-tuple (status, output). The locale encoding is used
        to decode the output and process newlines.
        
        A trailing newline is stripped from the output.
        The exit status for the command can be interpreted
        according to the rules for the function 'wait'. Example:
        
        >>> import subprocess
        >>> subprocess.getstatusoutput('ls /bin/ls')
        (0, '/bin/ls')
        >>> subprocess.getstatusoutput('cat /bin/junk')
        (1, 'cat: /bin/junk: No such file or directory')
        >>> subprocess.getstatusoutput('/bin/junk')
        (127, 'sh: /bin/junk: not found')
        >>> subprocess.getstatusoutput('/bin/kill $$')
        (-15, '')
    
    run(*popenargs, input=None, timeout=None, check=False, **kwargs)
        Run command with arguments and return a CompletedProcess instance.
        
        The returned instance will have attributes args, returncode, stdout and
        stderr. By default, stdout and stderr are not captured, and those attributes
        will be None. Pass stdout=PIPE and/or stderr=PIPE in order to capture them.
        
        If check is True and the exit code was non-zero, it raises a
        CalledProcessError. The CalledProcessError object will have the return code
        in the returncode attribute, and output & stderr attributes if those streams
        were captured.
        
        If timeout is given, and the process takes too long, a TimeoutExpired
        exception will be raised.
        
        There is an optional argument "input", allowing you to
        pass a string to the subprocess's stdin.  If you use this argument
        you may not also use the Popen constructor's "stdin" argument, as
        it will be used internally.
        
        The other arguments are the same as for the Popen constructor.
        
        If universal_newlines=True is passed, the "input" argument must be a
        string and stdout/stderr in the returned object will be strings rather than
        bytes.

DATA
    CREATE_NEW_CONSOLE = 16
    CREATE_NEW_PROCESS_GROUP = 512
    DEVNULL = -3
    PIPE = -1
    STARTF_USESHOWWINDOW = 1
    STARTF_USESTDHANDLES = 256
    STDOUT = -2
    STD_ERROR_HANDLE = 4294967284
    STD_INPUT_HANDLE = 4294967286
    STD_OUTPUT_HANDLE = 4294967285
    SW_HIDE = 0
    __all__ = ['Popen', 'PIPE', 'STDOUT', 'call', 'check_call', 'getstatus...

FILE
    c:\users\zombi\anaconda3\lib\subprocess.py



