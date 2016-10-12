﻿#region Licence
/* The MIT License (MIT)
Copyright © 2014 Ian Cooper <ian_hammond_cooper@yahoo.co.uk>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE. */

#endregion

using System;
using System.Threading;
using System.Threading.Tasks;
using paramore.brighter.commandprocessor;
using paramore.brighter.commandprocessor.Logging;

namespace paramore.brighter.commandprocessor.tests.nunit.CommandProcessors.TestDoubles
{
    internal class MyLoggingHandlerAsync<TRequest>: RequestHandlerAsync<TRequest>, IDisposable where TRequest : class, IRequest
    {
        private TRequest _command;
        public static bool DisposeWasCalled { get; set; }

        public MyLoggingHandlerAsync(ILog logger) : base(logger)
        {
            _command = null;
            DisposeWasCalled = false;
        }

        public override async Task<TRequest> HandleAsync(TRequest command, CancellationToken? ct = null)
        {
            if (ct.HasValue && ct.Value.IsCancellationRequested)
            {
                return command;
            }

            LogCommand(command);
            return await base.HandleAsync(command, ct).ConfigureAwait(base.ContinueOnCapturedContext);
        }

        public static bool Shouldreceive(TRequest expectedCommand)
        {
            return (expectedCommand != null);
        }

        private void LogCommand(TRequest request)
        {
            _command = request;
        }

        public void Dispose()
        {
            DisposeWasCalled = true;
        }
    }
}